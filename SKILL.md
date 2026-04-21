# MCP GMPY2

MCP server exposing gmpy2 arbitrary precision arithmetic functions.

## When to use this skill

Use this skill when you need to:
- Work with very large integers
- Perform primality tests
- Factor large numbers
- Compute GCD, modular inverses
- Calculate special functions (factorial, Fibonacci, etc.)

## Tools

- `mpz`, `mpq`, `mpfr` - Create arbitrary precision numbers
- `add`, `sub`, `mul`, `div`, `pow`, `powmod`, `mod` - Arithmetic
- `is_prime`, `is_probable_prime` - Primality tests
- `next_prime`, `prev_prime` - Prime navigation
- `prime_factors` - Factorization
- `gcd`, `lcm`, `gcdext`, `invert` - Number theory
- `fac`, `fib`, `luc`, `binomial` - Special functions
- `sqrt`, `is_square`, `is_power`, `iroot` - Roots
- `legendre`, `jacobi`, `kronecker` - Symbols
- `tonelli` - Square roots modulo prime
- `mobius`, `phi`, `divisors`, `num_divisors` - Arithmetic functions
- `partition` - Partition function
- `miller_rabin`, `lucas_lehmer` - Advanced primality tests
- `sieve` - Generate primes

## Install

```bash
pip install mcp-gmpy2
```