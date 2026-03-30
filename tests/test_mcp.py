"""Tests for mcp-gmpy2 tools."""

import pytest


class TestBasicArithmetic:
    """Test basic arithmetic operations."""

    def test_mpz(self):
        from mcp_gmpy2.mcp import mpz

        result = mpz("123456789012345678901234567890")
        assert result == "123456789012345678901234567890"

    def test_mpq(self):
        from mcp_gmpy2.mcp import mpq

        result = mpq(numer="1", denom="3")
        assert "1" in result and "3" in result

    def test_mpfr(self):
        from mcp_gmpy2.mcp import mpfr

        result = mpfr(n="3.14", prec=53)
        assert "3.14" in result

    def test_add(self):
        from mcp_gmpy2.mcp import add

        result = add(a="123", b="456")
        assert result == "579"

    def test_sub(self):
        from mcp_gmpy2.mcp import sub

        result = sub(a="456", b="123")
        assert result == "333"

    def test_mul(self):
        from mcp_gmpy2.mcp import mul

        result = mul(a="12", b="34")
        assert result == "408"

    def test_div(self):
        from mcp_gmpy2.mcp import div

        result = div(a="100", b="3")
        assert result == "33"

    def test_pow(self):
        from mcp_gmpy2.mcp import pow

        result = pow(base="2", exp="10")
        assert result == "1024"

    def test_powmod(self):
        from mcp_gmpy2.mcp import powmod

        result = powmod(base="2", exp="10", mod="1000")
        assert result == "24"

    def test_mod(self):
        from mcp_gmpy2.mcp import mod

        result = mod(a="100", b="7")
        assert result == "2"


class TestPrimality:
    """Test primality testing functions."""

    def test_is_prime_true(self):
        from mcp_gmpy2.mcp import is_prime

        result = is_prime(n="7")
        assert result is True

    def test_is_prime_false(self):
        from mcp_gmpy2.mcp import is_prime

        result = is_prime(n="8")
        assert result is False

    def test_is_probable_prime(self):
        from mcp_gmpy2.mcp import is_probable_prime

        result = is_probable_prime(n="2305843009213693951")
        assert result is True

    def test_next_prime(self):
        from mcp_gmpy2.mcp import next_prime

        result = next_prime(n="10")
        assert result == "11"

    def test_prev_prime(self):
        from mcp_gmpy2.mcp import prev_prime

        result = prev_prime(n="10")
        assert result == "7"

    def test_miller_rabin(self):
        from mcp_gmpy2.mcp import miller_rabin

        result = miller_rabin(n="7")
        assert result is True


class TestFactorization:
    """Test factorization functions."""

    def test_prime_factors(self):
        from mcp_gmpy2.mcp import prime_factors

        result = prime_factors(n="100")
        expected = [{"prime": 2, "exp": 2}, {"prime": 5, "exp": 2}]
        assert result == expected

    def test_divisors(self):
        from mcp_gmpy2.mcp import divisors

        result = divisors(n="12")
        assert result == ["1", "2", "3", "4", "6", "12"]

    def test_num_divisors(self):
        from mcp_gmpy2.mcp import num_divisors

        result = num_divisors(n="12")
        assert result == 6


class TestNumberTheory:
    """Test number theory functions."""

    def test_gcd(self):
        from mcp_gmpy2.mcp import gcd

        result = gcd(a="48", b="18")
        assert result == "6"

    def test_lcm(self):
        from mcp_gmpy2.mcp import lcm

        result = lcm(a="4", b="6")
        assert result == "12"

    def test_gcdext(self):
        from mcp_gmpy2.mcp import gcdext

        result = gcdext(a="48", b="18")
        assert result == {"g": 6, "x": -1, "y": 3}

    def test_invert(self):
        from mcp_gmpy2.mcp import invert

        result = invert(a="3", m="11")
        assert result == "4"

    def test_fac(self):
        from mcp_gmpy2.mcp import fac

        result = fac(n="5")
        assert result == "120"

    def test_fib(self):
        from mcp_gmpy2.mcp import fib

        result = fib(n="10")
        assert result == "55"

    def test_luc(self):
        from mcp_gmpy2.mcp import luc

        result = luc(n="10")
        assert result == "123"

    def test_binomial(self):
        from mcp_gmpy2.mcp import binomial

        result = binomial(n="10", k="5")
        assert result == "252"

    def test_phi(self):
        from mcp_gmpy2.mcp import phi

        result = phi(n="10")
        assert result == "4"

    def test_sum_divisors(self):
        from mcp_gmpy2.mcp import sum_divisors

        result = sum_divisors(n="12")
        assert result == "28"


class TestRootAndPower:
    """Test root and power functions."""

    def test_sqrt(self):
        from mcp_gmpy2.mcp import sqrt

        result = sqrt(n="100")
        assert result == "10"

    def test_is_square(self):
        from mcp_gmpy2.mcp import is_square

        result = is_square(n="100")
        assert result is True

    def test_is_power(self):
        from mcp_gmpy2.mcp import is_power

        result = is_power(n="64")
        assert result is True

    def test_iroot(self):
        from mcp_gmpy2.mcp import iroot

        result = iroot(n="27", r=3)
        assert result == {"root": 3, "exact": True}

    def test_num_digits(self):
        from mcp_gmpy2.mcp import num_digits

        result = num_digits(n="12345")
        assert result == 5

    def test_num_bits(self):
        from mcp_gmpy2.mcp import num_bits

        result = num_bits(n="255")
        assert result == 8


class TestSymbols:
    """Test Legendre, Jacobi, and Kronecker symbols."""

    def test_legendre(self):
        from mcp_gmpy2.mcp import legendre

        result = legendre(a="3", p="7")
        assert result == -1

    def test_jacobi(self):
        from mcp_gmpy2.mcp import jacobi

        result = jacobi(a="3", n="7")
        assert result == -1

    def test_kronecker(self):
        from mcp_gmpy2.mcp import kronecker

        result = kronecker(a="3", n="7")
        assert result == -1


class TestOtherFunctions:
    """Test other mathematical functions."""

    def test_mobius(self):
        from mcp_gmpy2.mcp import mobius

        result = mobius(n="30")
        assert result == -1

    def test_partition(self):
        from mcp_gmpy2.mcp import partition

        result = partition(n="5")
        assert result == "7"

    def test_is_smooth(self):
        from mcp_gmpy2.mcp import is_smooth

        result = is_smooth(n="100", bound=5)
        assert result is True

    def test_is_sophie_germain(self):
        from mcp_gmpy2.mcp import is_sophie_germain

        result = is_sophie_germain(p="5")
        assert result is True

    def test_is_safe_prime(self):
        from mcp_gmpy2.mcp import is_safe_prime

        result = is_safe_prime(p="7")
        assert result is True

    def test_lucas_lehmer(self):
        from mcp_gmpy2.mcp import lucas_lehmer

        result = lucas_lehmer(p="127")
        assert result is True

    def test_sieve(self):
        from mcp_gmpy2.mcp import sieve

        result = sieve(limit="30")
        assert result == ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29"]

    def test_tonelli(self):
        from mcp_gmpy2.mcp import tonelli

        result = tonelli(n="1", p="7")
        assert result == "1"


class TestEdgeCases:
    """Test edge cases."""

    def test_zero_division(self):
        from mcp_gmpy2.mcp import div

        with pytest.raises(ZeroDivisionError):
            div(a="1", b="0")

    def test_mod_by_zero(self):
        from mcp_gmpy2.mcp import mod

        with pytest.raises(ZeroDivisionError):
            mod(a="1", b="0")

    def test_invert_no_inverse(self):
        from mcp_gmpy2.mcp import invert

        result = invert(a="2", m="4")
        assert result is None

    def test_very_large_numbers(self):
        from mcp_gmpy2.mcp import add, fac

        large_num = "123456789012345678901234567890"
        result = add(a=large_num, b="1")
        assert result == "123456789012345678901234567891"
        result = fac(n="20")
        assert result == "2432902008176640000"

    def test_invalid_primality_input(self):
        from mcp_gmpy2.mcp import is_prime

        result = is_prime(n="1")
        assert result is False
        result = is_prime(n="0")
        assert result is False

    def test_negative_powmod(self):
        from mcp_gmpy2.mcp import powmod

        result = powmod(base="-2", exp="4", mod="5")
        assert result == "1"

    def test_sieve_small_limit(self):
        from mcp_gmpy2.mcp import sieve

        result = sieve(limit="2")
        assert result == ["2"]

    def test_iroot_not_perfect(self):
        from mcp_gmpy2.mcp import iroot

        result = iroot(n="10", r=2)
        assert result == {"root": 3, "exact": False}

    def test_is_square_false(self):
        from mcp_gmpy2.mcp import is_square

        result = is_square(n="10")
        assert result is False

    def test_is_power_false(self):
        from mcp_gmpy2.mcp import is_power

        result = is_power(n="10")
        assert result is False

    def test_mobius_square_free(self):
        from mcp_gmpy2.mcp import mobius

        result = mobius(n="6")
        assert result == 1

    def test_mobius_with_squared_factor(self):
        from mcp_gmpy2.mcp import mobius

        result = mobius(n="12")
        assert result == 0

    def test_tonelli_with_root(self):
        from mcp_gmpy2.mcp import tonelli

        result = tonelli(n="2", p="7")
        assert result is not None

    def test_prev_prime_3(self):
        from mcp_gmpy2.mcp import prev_prime

        result = prev_prime(n="5")
        assert result == "3"
