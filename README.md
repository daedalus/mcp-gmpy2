# mcp-gmpy2

> MCP server exposing gmpy2 arbitrary precision arithmetic functions

[![PyPI](https://img.shields.io/pypi/v/mcp-gmpy2.svg)](https://pypi.org/project/mcp-gmpy2/)
[![Python](https://img.shields.io/pypi/pyversions/mcp-gmpy2.svg)](https://pypi.org/project/mcp-gmpy2/)
[![Coverage](https://codecov.io/gh/daedalus/mcp-gmpy2/branch/main/graph/badge.svg)](https://codecov.io/gh/daedalus/mcp-gmpy2)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

mcp-name: io.github.daedalus/mcp-gmpy2

## Install

```bash
pip install mcp-gmpy2
```

## Usage

```bash
# Run as stdio server
mcp-gmpy2
```

## Available Tools

- `mpz` - Create arbitrary precision integer
- `mpq` - Create arbitrary precision rational
- `mpfr` - Create arbitrary precision floating-point
- `add` - Add two arbitrary precision integers
- `sub` - Subtract two arbitrary precision integers
- `mul` - Multiply two arbitrary precision integers
- `div` - Divide two arbitrary precision integers
- `pow` - Power operation with arbitrary precision
- `powmod` - Modular exponentiation
- `mod` - Modulo operation
- `is_prime` - Primality test
- `is_probable_prime` - Probabilistic primality test
- `next_prime` - Next prime after n
- `prev_prime` - Previous prime before n
- `prime_factors` - Get prime factorization
- `gcd` - Greatest common divisor
- `lcm` - Least common multiple
- `gcdext` - Extended GCD
- `invert` - Modular inverse
- `fac` - Factorial
- `fib` - Fibonacci number
- `luc` - Lucas number
- `binomial` - Binomial coefficient
- `sqrt` - Integer square root
- `is_square` - Check if perfect square
- `is_power` - Check if perfect power
- `iroot` - Integer n-th root
- `num_digits` - Number of digits
- `num_bits` - Number of bits
- `legendre` - Legendre symbol
- `jacobi` - Jacobi symbol
- `kronecker` - Kronecker symbol
- `tonelli` - Tonelli-Shanks square root
- `mobius` - Mobius function
- `phi` - Euler's totient
- `divisors` - All divisors
- `num_divisors` - Count of divisors
- `sum_divisors` - Sum of divisors
- `partition` - Partition function p(n)
- `is_smooth` - Check if B-smooth
- `is_sophie_germain` - Sophie Germain prime test
- `is_safe_prime` - Safe prime test
- `miller_rabin` - Miller-Rabin primality test
- `lucas_lehmer` - Lucas-Lehmer primality test for Mersenne
- `sieve` - Generate primes up to n

## Development

```bash
git clone https://github.com/daedalus/mcp-gmpy2.git
cd mcp-gmpy2
pip install -e ".[test]"

# run tests
pytest

# format
ruff format src/ tests/

# lint
ruff check src/ tests/

# type check
mypy src/
```
