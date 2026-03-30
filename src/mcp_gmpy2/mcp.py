"""MCP server exposing gmpy2 arbitrary precision arithmetic functions."""

import builtins

import gmpy2
from fastmcp import FastMCP

mcp = FastMCP("mcp-gmpy2")


@mcp.tool()
def mpz(n: str) -> str:
    """Create an arbitrary precision integer from a string.

    Args:
        n: String representation of an integer (can be very large).

    Returns:
        String representation of the arbitrary precision integer.

    Example:
        >>> mpz("123456789012345678901234567890")
        "123456789012345678901234567890"
    """
    return str(gmpy2.mpz(n))


@mcp.tool()
def mpq(numer: str, denom: str) -> str:
    """Create an arbitrary precision rational number.

    Args:
        numer: String representation of the numerator.
        denom: String representation of the denominator (must not be zero).

    Returns:
        String representation of the rational number.

    Example:
        >>> mpq("1", "3")
        "mpq(1,3)"
    """
    return str(gmpy2.mpq(int(numer), int(denom)))


@mcp.tool()
def mpfr(n: str, prec: int = 256) -> str:
    """Create an arbitrary precision floating-point number.

    Args:
        n: String representation of the number.
        prec: Precision in bits (default: 256).

    Returns:
        String representation of the floating-point number.

    Example:
        >>> mpfr("3.141592653589793238462643383279")
        "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899"
    """
    return str(gmpy2.mpfr(n, precision=prec))


@mcp.tool()
def add(a: str, b: str) -> str:
    """Add two arbitrary precision integers.

    Args:
        a: First integer as string.
        b: Second integer as string.

    Returns:
        Sum as string.

    Example:
        >>> add("12345678901234567890", "98765432109876543210")
        "111111111011111111100"
    """
    return str(gmpy2.mpz(a) + gmpy2.mpz(b))


@mcp.tool()
def sub(a: str, b: str) -> str:
    """Subtract two arbitrary precision integers.

    Args:
        a: First integer as string.
        b: Second integer as string.

    Returns:
        Difference as string.

    Example:
        >>> sub("98765432109876543210", "12345678901234567890")
        "86419753208641975320"
    """
    return str(gmpy2.mpz(a) - gmpy2.mpz(b))


@mcp.tool()
def mul(a: str, b: str) -> str:
    """Multiply two arbitrary precision integers.

    Args:
        a: First integer as string.
        b: Second integer as string.

    Returns:
        Product as string.

    Example:
        >>> mul("123456789", "987654321")
        "121932631137021795226185032733276203"
    """
    return str(gmpy2.mpz(a) * gmpy2.mpz(b))


@mcp.tool()
def div(a: str, b: str) -> str:
    """Divide two arbitrary precision integers (integer division).

    Args:
        a: Dividend as string.
        b: Divisor as string (must not be zero).

    Returns:
        Quotient as string.

    Example:
        >>> div("123456789", "456")
        "270807"
    """
    return str(gmpy2.mpz(a) // gmpy2.mpz(b))


@mcp.tool()
def pow(base: str, exp: str) -> str:
    """Compute power with arbitrary precision integers.

    Args:
        base: Base as string.
        exp: Exponent as string (non-negative integer).

    Returns:
        Result as string.

    Example:
        >>> pow("2", "100")
        "1267650600228229401496703205376"
    """
    return str(gmpy2.mpz(base) ** int(exp))


@mcp.tool()
def powmod(base: str, exp: str, mod: str) -> str:
    """Compute modular exponentiation (base^exp mod mod).

    Args:
        base: Base as string.
        exp: Exponent as string.
        mod: Modulus as string (must be positive).

    Returns:
        Result as string.

    Example:
        >>> powmod("2", "1000000000", "1000000007")
        "362486309"
    """
    return str(gmpy2.powmod(gmpy2.mpz(base), gmpy2.mpz(exp), gmpy2.mpz(mod)))


@mcp.tool()
def mod(a: str, b: str) -> str:
    """Compute modulo operation.

    Args:
        a: Dividend as string.
        b: Divisor as string (must not be zero).

    Returns:
        Remainder as string.

    Example:
        >>> mod("123456789", "456")
        "333"
    """
    return str(gmpy2.mpz(a) % gmpy2.mpz(b))


@mcp.tool()
def is_prime(n: str) -> bool:
    """Test if n is prime using deterministic method.

    Args:
        n: Integer to test as string.

    Returns:
        True if prime, False otherwise.

    Example:
        >>> is_prime("7")
        True
    """
    return gmpy2.is_prime(gmpy2.mpz(n))  # type: ignore[no-any-return]


@mcp.tool()
def is_probable_prime(n: str, rounds: int = 25) -> bool:
    """Test if n is probably prime using Miller-Rabin.

    Args:
        n: Integer to test as string.
        rounds: Number of Miller-Rabin rounds (default: 25).

    Returns:
        True if probably prime, False otherwise.

    Example:
        >>> is_probable_prime("2305843009213693951")
        True
    """
    result = gmpy2.is_probab_prime(gmpy2.mpz(n), rounds)
    return result != 0  # type: ignore[no-any-return]


@mcp.tool()
def next_prime(n: str) -> str:
    """Find the next prime after n.

    Args:
        n: Integer as string.

    Returns:
        Next prime as string.

    Example:
        >>> next_prime("100")
        "101"
    """
    return str(gmpy2.next_prime(gmpy2.mpz(n)))


@mcp.tool()
def prev_prime(n: str) -> str:
    """Find the previous prime before n.

    Args:
        n: Integer greater than 2 as string.

    Returns:
        Previous prime as string.

    Example:
        >>> prev_prime("100")
        "97"
    """
    return str(gmpy2.prev_prime(gmpy2.mpz(n)))


@mcp.tool()
def prime_factors(n: str) -> list[dict[str, int]]:
    """Get prime factorization of n.

    Args:
        n: Integer to factor as string (n > 0).

    Returns:
        List of dictionaries with prime and exponent.

    Example:
        >>> prime_factors("100")
        [{"prime": 2, "exp": 2}, {"prime": 5, "exp": 2}]
    """
    n_val = int(n)
    factors: dict[int, int] = {}
    d = 2
    while d * d <= n_val:
        while n_val % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n_val //= d
        d += 1
    if n_val > 1:
        factors[n_val] = factors.get(n_val, 0) + 1
    return [{"prime": p, "exp": e} for p, e in factors.items()]


@mcp.tool()
def gcd(a: str, b: str) -> str:
    """Compute greatest common divisor.

    Args:
        a: First integer as string.
        b: Second integer as string.

    Returns:
        GCD as string.

    Example:
        >>> gcd("48", "18")
        "6"
    """
    return str(gmpy2.gcd(gmpy2.mpz(a), gmpy2.mpz(b)))


@mcp.tool()
def lcm(a: str, b: str) -> str:
    """Compute least common multiple.

    Args:
        a: First integer as string.
        b: Second integer as string.

    Returns:
        LCM as string.

    Example:
        >>> lcm("4", "6")
        "12"
    """
    return str(gmpy2.lcm(gmpy2.mpz(a), gmpy2.mpz(b)))


@mcp.tool()
def gcdext(a: str, b: str) -> dict[str, int]:
    """Compute extended GCD (gcd(a,b) = ax + by).

    Args:
        a: First integer as string.
        b: Second integer as string.

    Returns:
        Dictionary with g, x, y where g = gcd(a,b) and ax + by = g.

    Example:
        >>> gcdext("48", "18")
        {"g": 6, "x": -1, "y": 3}
    """
    g, x, y = gmpy2.gcdext(gmpy2.mpz(a), gmpy2.mpz(b))
    return {"g": int(g), "x": int(x), "y": int(y)}


@mcp.tool()
def invert(a: str, m: str) -> str | None:
    """Compute modular inverse (a^(-1) mod m).

    Args:
        a: Integer as string.
        m: Modulus as string (must be positive and coprime to a).

    Returns:
        Modular inverse as string, or None if no inverse exists.

    Example:
        >>> invert("3", "11")
        "4"
    """
    try:
        result = gmpy2.invert(gmpy2.mpz(a), gmpy2.mpz(m))
        return str(result)
    except ZeroDivisionError:
        return None


@mcp.tool()
def fac(n: str) -> str:
    """Compute factorial n!.

    Args:
        n: Non-negative integer as string.

    Returns:
        Factorial as string.

    Example:
        >>> fac("100")
        "93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000"
    """
    return str(gmpy2.fac(int(n)))


@mcp.tool()
def fib(n: str) -> str:
    """Compute nth Fibonacci number.

    Args:
        n: Non-negative integer as string.

    Returns:
        nth Fibonacci number as string.

    Example:
        >>> fib("100")
        "354224848179261915075"
    """
    return str(gmpy2.fib(int(n)))


@mcp.tool()
def luc(n: str) -> str:
    """Compute nth Lucas number.

    Args:
        n: Non-negative integer as string.

    Returns:
        nth Lucas number as string.

    Example:
        >>> luc("100")
        "792070839848372253127"
    """
    return str(gmpy2.lucas(int(n)))


@mcp.tool()
def binomial(n: str, k: str) -> str:
    """Compute binomial coefficient C(n,k).

    Args:
        n: Non-negative integer as string.
        k: Non-negative integer as string.

    Returns:
        Binomial coefficient as string.

    Example:
        >>> binomial("100", "50")
        "100891344545564193334812497256"
    """
    return str(gmpy2.comb(int(n), int(k)))


@mcp.tool()
def sqrt(n: str) -> str:
    """Compute integer square root (floor of sqrt(n)).

    Args:
        n: Non-negative integer as string.

    Returns:
        Integer square root as string.

    Example:
        >>> sqrt("100")
        "10"
    """
    return str(gmpy2.isqrt(gmpy2.mpz(n)))


@mcp.tool()
def is_square(n: str) -> bool:
    """Check if n is a perfect square.

    Args:
        n: Non-negative integer as string.

    Returns:
        True if perfect square, False otherwise.

    Example:
        >>> is_square("100")
        True
    """
    return gmpy2.is_square(gmpy2.mpz(n))  # type: ignore[no-any-return]


@mcp.tool()
def is_power(n: str) -> bool:
    """Check if n is a perfect power.

    Args:
        n: Integer as string (n > 0).

    Returns:
        True if perfect power, False otherwise.

    Example:
        >>> is_power("64")
        True
    """
    return gmpy2.is_power(gmpy2.mpz(n))  # type: ignore[no-any-return]


@mcp.tool()
def iroot(n: str, r: int = 2) -> dict[str, int | bool]:
    """Compute integer r-th root.

    Args:
        n: Non-negative integer as string.
        r: Root degree (default: 2).

    Returns:
        Dictionary with root and exact boolean.

    Example:
        >>> iroot("27", "3")
        {"root": 3, "exact": true}
    """
    root, exact = gmpy2.iroot(gmpy2.mpz(n), r)
    return {"root": int(root), "exact": bool(exact)}


@mcp.tool()
def num_digits(n: str, base: int = 10) -> int:
    """Count number of digits in n.

    Args:
        n: Integer as string.
        base: Base for digit counting (default: 10).

    Returns:
        Number of digits.

    Example:
        >>> num_digits("1234567890")
        10
    """
    return gmpy2.mpz(n).num_digits(base)  # type: ignore[no-any-return]


@mcp.tool()
def num_bits(n: str) -> int:
    """Count number of bits in n.

    Args:
        n: Integer as string.

    Returns:
        Number of bits.

    Example:
        >>> num_bits("255")
        8
    """
    return gmpy2.mpz(n).bit_length()  # type: ignore[no-any-return]


@mcp.tool()
def legendre(a: str, p: str) -> int:
    """Compute Legendre symbol (a/p).

    Args:
        a: Integer as string.
        p: Odd prime as string.

    Returns:
        1, -1, or 0.

    Example:
        >>> legendre("3", "7")
        -1
    """
    return int(gmpy2.legendre(gmpy2.mpz(a), gmpy2.mpz(p)))


@mcp.tool()
def jacobi(a: str, n: str) -> int:
    """Compute Jacobi symbol (a/n).

    Args:
        a: Integer as string.
        n: Positive odd integer as string.

    Returns:
        1, -1, or 0.

    Example:
        >>> jacobi("3", "7")
        -1
    """
    return int(gmpy2.jacobi(gmpy2.mpz(a), gmpy2.mpz(n)))


@mcp.tool()
def kronecker(a: str, n: str) -> int:
    """Compute Kronecker symbol (a/n).

    Args:
        a: Integer as string.
        n: Integer as string.

    Returns:
        1, -1, or 0.

    Example:
        >>> kronecker("3", "7")
        -1
    """
    return int(gmpy2.kronecker(gmpy2.mpz(a), gmpy2.mpz(n)))


@mcp.tool()
def tonelli(n: str, p: str) -> str | None:
    """Compute modular square root using Tonelli-Shanks.

    Args:
        n: Quadratic residue as string.
        p: Odd prime as string.

    Returns:
        Square root as string, or None if no square root exists.

    Example:
        >>> tonelli("3", "7")
        "5"
    """
    n_val = int(n)
    p_val = int(p)
    if n_val >= p_val:
        n_val = n_val % p_val
    if builtins.pow(n_val, (p_val - 1) // 2, p_val) != 1:
        return None
    if p_val % 4 == 3:
        return str(builtins.pow(n_val, (p_val + 1) // 4, p_val))
    q = p_val - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while builtins.pow(z, (p_val - 1) // 2, p_val) != p_val - 1:
        z += 1
    c = builtins.pow(z, q, p_val)
    x = builtins.pow(n_val, (q + 1) // 2, p_val)
    t = builtins.pow(n_val, q, p_val)
    m = s
    while t != 1:
        i = 1
        while i < m:
            if builtins.pow(t, 2**i, p_val) == 1:
                break
            i += 1
        b = builtins.pow(c, 2 ** (m - i - 1), p_val)
        x = (x * b) % p_val
        t = (t * b * b) % p_val
        c = builtins.pow(b, 2, p_val)
        m = i
    if x == p_val - x:
        return str(p_val - x)
    return str(x)


@mcp.tool()
def mobius(n: str) -> int:
    """Compute Mobius function.

    Args:
        n: Positive integer as string.

    Returns:
        1 if n is square-free with even prime count, -1 if odd, 0 if has squared factor.

    Example:
        >>> mobius("30")
        -1
    """
    n_val = int(n)
    if n_val == 1:
        return 1
    factors = 0
    p = 2
    temp = n_val
    while p * p <= temp:
        if temp % p == 0:
            temp //= p
            if temp % p == 0:
                return 0
            factors += 1
        p += 1
    if temp > 1:
        factors += 1
    return -1 if factors % 2 else 1


@mcp.tool()
def phi(n: str) -> str:
    """Compute Euler's totient function phi(n).

    Args:
        n: Positive integer as string.

    Returns:
        phi(n) as string.

    Example:
        >>> phi("10")
        "4"
    """
    n_val = int(n)
    result = n_val
    temp = n_val
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return str(result)


@mcp.tool()
def divisors(n: str) -> list[str]:
    """Get all positive divisors of n.

    Args:
        n: Positive integer as string.

    Returns:
        List of divisors as strings.

    Example:
        >>> divisors("12")
        ["1", "2", "3", "4", "6", "12"]
    """
    n_val = int(n)
    divs = []
    for i in range(1, int(n_val**0.5) + 1):
        if n_val % i == 0:
            divs.append(str(i))
            if i != n_val // i:
                divs.append(str(n_val // i))
    return sorted(divs, key=lambda x: int(x))


@mcp.tool()
def num_divisors(n: str) -> int:
    """Count number of positive divisors of n.

    Args:
        n: Positive integer as string.

    Returns:
        Number of divisors.

    Example:
        >>> num_divisors("12")
        6
    """
    n_val = int(n)
    count = 0
    for i in range(1, int(n_val**0.5) + 1):
        if n_val % i == 0:
            count += 1
            if i != n_val // i:
                count += 1
    return count


@mcp.tool()
def sum_divisors(n: str) -> str:
    """Compute sum of positive divisors of n.

    Args:
        n: Positive integer as string.

    Returns:
        Sum of divisors as string.

    Example:
        >>> sum_divisors("12")
        "28"
    """
    n_val = int(n)
    total = 0
    for i in range(1, int(n_val**0.5) + 1):
        if n_val % i == 0:
            total += i
            if i != n_val // i:
                total += n_val // i
    return str(total)


@mcp.tool()
def partition(n: str) -> str:
    """Compute partition function p(n).

    Args:
        n: Non-negative integer as string.

    Returns:
        p(n) as string.

    Example:
        >>> partition("5")
        "7"
    """
    n_val = int(n)
    partitions = [0] * (n_val + 1)
    partitions[0] = 1
    for i in range(1, n_val + 1):
        for j in range(i, n_val + 1):
            partitions[j] += partitions[j - i]
    return str(partitions[n_val])


def _is_prime_check(x: int) -> bool:
    """Check if x is prime."""
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


@mcp.tool()
def is_smooth(n: str, bound: int) -> bool:
    """Check if n is B-smooth (all prime factors <= bound).

    Args:
        n: Positive integer as string.
        bound: Smoothness bound.

    Returns:
        True if B-smooth, False otherwise.

    Example:
        >>> is_smooth("100", "5")
        True
    """
    n_val = int(n)
    if n_val <= bound:
        return True
    d = 2
    while d * d <= n_val:
        while n_val % d == 0:
            if d > bound:
                return False
            n_val //= d
        d += 1
    return n_val <= bound if n_val > 1 else True


@mcp.tool()
def is_sophie_germain(p: str) -> bool:
    """Check if p is a Sophie Germain prime (p and 2p+1 both prime).

    Args:
        p: Prime candidate as string.

    Returns:
        True if Sophie Germain prime, False otherwise.

    Example:
        >>> is_sophie_germain("5")
        True
    """
    p_val = int(p)
    if not _is_prime_check(p_val):
        return False
    return _is_prime_check(2 * p_val + 1)


@mcp.tool()
def is_safe_prime(p: str) -> bool:
    """Check if p is a safe prime (p = 2q + 1 where q is prime).

    Args:
        p: Prime candidate as string.

    Returns:
        True if safe prime, False otherwise.

    Example:
        >>> is_safe_prime("7")
        True
    """
    p_val = int(p)
    if p_val < 5:
        return False
    q = (p_val - 1) // 2
    return _is_prime_check(q) and _is_prime_check(p_val)


@mcp.tool()
def miller_rabin(n: str, rounds: int = 25) -> bool:
    """Miller-Rabin primality test.

    Args:
        n: Integer to test as string.
        rounds: Number of rounds (default: 25).

    Returns:
        True if probably prime, False otherwise.

    Example:
        >>> miller_rabin("2305843009213693951")
        True
    """
    result = gmpy2.is_probab_prime(gmpy2.mpz(n), rounds)
    return result != 0  # type: ignore[no-any-return]


@mcp.tool()
def lucas_lehmer(p: str) -> bool:
    """Lucas-Lehmer primality test for Mersenne primes.

    Args:
        p: Prime exponent as string (tests if 2^p - 1 is prime).

    Returns:
        True if Mersenne prime, False otherwise.

    Example:
        >>> lucas_lehmer("127")
        True
    """
    p_val = int(p)
    if p_val < 2:
        return False
    if p_val == 2:
        return True
    m = (1 << p_val) - 1
    s = 4
    for _ in range(p_val - 2):
        s = (s * s - 2) % m
    return s == 0


def _simple_sieve(limit: int) -> list[int]:
    """Simple sieve of Eratosthenes."""
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]


@mcp.tool()
def sieve(limit: str) -> list[str]:
    """Generate all primes up to limit using sieve.

    Args:
        limit: Upper limit as string.

    Returns:
        List of primes as strings.

    Example:
        >>> sieve("30")
        ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29"]
    """
    return [str(p) for p in _simple_sieve(int(limit))]
