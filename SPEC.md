# SPEC.md — mcp-gmpy2

## Purpose
MCP server that exposes gmpy2 arbitrary precision arithmetic functions as tools, enabling large integer operations, prime number functions, modular arithmetic, and high-precision floating-point computations through the Model Context Protocol.

## Scope
- **In scope:**
  - Integer arithmetic (add, sub, mul, div, pow, mod)
  - Prime number functions (is_prime, next_prime, prev_prime, prime_factors, etc.)
  - Modular arithmetic (powmod, inversemod, gcdext)
  - Rational number operations
  - High-precision floating-point operations
  - Bit operations on large integers
  - Number theory functions (gcd, lcm, factorial, fibonacci, etc.)
- **Not in scope:**
  - Direct GMP library low-level bindings
  - Polynomials over finite fields
  - Algebraic number field operations

## Public API / Interface

### Tools (MCP)
All tools are exposed via fastmcp and accept JSON-serializable arguments.

| Function | Description |
|----------|-------------|
| `mpz` | Create arbitrary precision integer |
| `mpq` | Create arbitrary precision rational |
| `mpfr` | Create arbitrary precision floating-point |
| `add` | Add two arbitrary precision numbers |
| `sub` | Subtract two arbitrary precision numbers |
| `mul` | Multiply two arbitrary precision numbers |
| `div` | Divide two arbitrary precision numbers |
| `pow` | Power operation with arbitrary precision |
| `powmod` | Modular exponentiation |
| `mod` | Modulo operation |
| `is_prime` | Primality test |
| `is_probable_prime` | Probabilistic primality test |
| `next_prime` | Next prime after n |
| `prev_prime` | Previous prime before n |
| `prime_factors` | Get prime factorization |
| `gcd` | Greatest common divisor |
| `lcm` | Least common multiple |
| `gcdext` | Extended GCD |
| `invert` | Modular inverse |
| `fac` | Factorial |
| `fib` | Fibonacci number |
| `luc` | Lucas number |
| `binomial` | Binomial coefficient |
| `sqrt` | Integer square root |
| `is_square` | Check if perfect square |
| `is_power` | Check if perfect power |
| `iroot` | Integer n-th root |
| `num_digits` | Number of digits |
| `num_bits` | Number of bits |
| `legendre` | Legendre symbol |
| `jacobi` | Jacobi symbol |
| `kronecker` | Kronecker symbol |
| `tonelli` | Tonelli-Shanks square root |
| `mobius` | Mobius function |
| `phi` | Euler's totient |
| `divisors` | All divisors |
| `num_divisors` | Count of divisors |
| `sum_divisors` | Sum of divisors |
| `partition` | Partition function p(n) |
| `is_smooth` | Check if B-smooth |
| `is_sophie_germain` | Sophie Germain prime test |
| `is_safe_prime` | Safe prime test |
| `miller_rabin` | Miller-Rabin primality test |
| `lucas_lehmer` | Lucas-Lehmer primality test for Mersenne |
| `sieve` | Generate primes up to n |

## Data Formats
- Inputs: JSON numbers (as strings for large values) or JSON integers
- Outputs: JSON numbers (as strings for large values) or JSON integers

## Edge Cases
- Handle zero division (raise error)
- Handle negative modular inverse (return positive result)
- Handle very large numbers (use gmpy2 internally)
- Handle non-integer inputs for integer functions (raise TypeError)
- Handle invalid primality inputs (n < 2)
- Handle empty factor lists
- Handle negative bases in powmod with even exponent

## Performance & Constraints
- All arithmetic uses gmpy2's optimized C implementation
- No artificial limits on number size (GMP handles it)
- Primality tests use probabilistic methods for large numbers
