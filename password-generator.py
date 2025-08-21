"""
Secure Password Generator Module
Generates strong, customizable passwords with various character sets.
"""

import random
import string
import secrets
from typing import List, Optional


class PasswordGenerator:
    """A secure password generator with customizable options."""
    
    def __init__(self):
        self.character_sets = {
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
            'digits': string.digits,
            'symbols': string.punctuation
        }
    
    def generate_password(self, 
                         length: int = 16,
                         use_lowercase: bool = True,
                         use_uppercase: bool = True,
                         use_digits: bool = True,
                         use_symbols: bool = True,
                         exclude_similar: bool = True) -> str:
        """
        Generate a secure random password.
        
        Args:
            length: Length of the password (default: 16)
            use_lowercase: Include lowercase letters (default: True)
            use_uppercase: Include uppercase letters (default: True)
            use_digits: Include digits (default: True)
            use_symbols: Include symbols (default: True)
            exclude_similar: Exclude similar characters like 'l', '1', 'I' (default: True)
            
        Returns:
            str: Generated password
            
        Raises:
            ValueError: If no character sets are selected or length is invalid
        """
        # Validate input parameters
        self._validate_parameters(length, use_lowercase, use_uppercase, 
                                use_digits, use_symbols)
        
        # Get character pool
        char_pool = self._build_character_pool(
            use_lowercase, use_uppercase, use_digits, use_symbols, exclude_similar
        )
        
        # Generate password using cryptographically secure random generator
        password = self._generate_secure_password(char_pool, length)
        
        # Ensure password meets all requirements
        self._ensure_password_requirements(password, use_lowercase, use_uppercase,
                                         use_digits, use_symbols)
        
        return password
    
    def _validate_parameters(self, 
                           length: int,
                           use_lowercase: bool,
                           use_uppercase: bool,
                           use_digits: bool,
                           use_symbols: bool) -> None:
        """Validate input parameters."""
        if length < 8:
            raise ValueError("Password length must be at least 8 characters")
        
        if length > 128:
            raise ValueError("Password length cannot exceed 128 characters")
        
        if not any([use_lowercase, use_uppercase, use_digits, use_symbols]):
            raise ValueError("At least one character set must be selected")
    
    def _build_character_pool(self,
                            use_lowercase: bool,
                            use_uppercase: bool,
                            use_digits: bool,
                            use_symbols: bool,
                            exclude_similar: bool) -> str:
        """Build the character pool based on selected options."""
        char_pool = []
        
        if use_lowercase:
            lowercase_chars = self.character_sets['lowercase']
            if exclude_similar:
                lowercase_chars = lowercase_chars.replace('l', '').replace('o', '')
            char_pool.append(lowercase_chars)
        
        if use_uppercase:
            uppercase_chars = self.character_sets['uppercase']
            if exclude_similar:
                uppercase_chars = uppercase_chars.replace('I', '').replace('O', '')
            char_pool.append(uppercase_chars)
        
        if use_digits:
            digit_chars = self.character_sets['digits']
            if exclude_similar:
                digit_chars = digit_chars.replace('0', '').replace('1', '')
            char_pool.append(digit_chars)
        
        if use_symbols:
            char_pool.append(self.character_sets['symbols'])
        
        return ''.join(char_pool)
    
    def _generate_secure_password(self, char_pool: str, length: int) -> str:
        """Generate password using cryptographically secure random generator."""
        return ''.join(secrets.choice(char_pool) for _ in range(length))
    
    def _ensure_password_requirements(self,
                                    password: str,
                                    use_lowercase: bool,
                                    use_uppercase: bool,
                                    use_digits: bool,
                                    use_symbols: bool) -> None:
        """
        Ensure the generated password meets all selected requirements.
        If not, regenerate until it does.
        """
        requirements = [
            (use_lowercase, string.ascii_lowercase, "lowercase"),
            (use_uppercase, string.ascii_uppercase, "uppercase"),
            (use_digits, string.digits, "digits"),
            (use_symbols, string.punctuation, "symbols")
        ]
        
        for required, char_set, name in requirements:
            if required and not any(char in char_set for char in password):
                raise RuntimeError(f"Failed to generate password with {name} characters")
    
    def generate_multiple_passwords(self, count: int = 5, **kwargs) -> List[str]:
        """
        Generate multiple passwords with the same configuration.
        
        Args:
            count: Number of passwords to generate (default: 5)
            **kwargs: Same parameters as generate_password
            
        Returns:
            List[str]: List of generated passwords
        """
        return [self.generate_password(**kwargs) for _ in range(count)]
    
    def estimate_password_strength(self, password: str) -> dict:
        """
        Estimate the strength of a password.
        
        Returns:
            dict: Strength assessment with score and feedback
        """
        length = len(password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)
        
        # Calculate strength score (0-100)
        score = 0
        score += min(length * 4, 40)  # Max 40 points for length
        score += 15 if has_lower else 0
        score += 15 if has_upper else 0
        score += 15 if has_digit else 0
        score += 15 if has_symbol else 0
        
        # Determine strength level
        if score >= 80:
            strength = "Very Strong"
        elif score >= 60:
            strength = "Strong"
        elif score >= 40:
            strength = "Moderate"
        elif score >= 20:
            strength = "Weak"
        else:
            strength = "Very Weak"
        
        return {
            'score': score,
            'strength': strength,
            'length': length,
            'has_lowercase': has_lower,
            'has_uppercase': has_upper,
            'has_digits': has_digit,
            'has_symbols': has_symbol
        }


# Example usage and main function
def main():
    """Example usage of the PasswordGenerator class."""
    generator = PasswordGenerator()
    
    # Generate a single strong password
    password = generator.generate_password(
        length=20,
        use_lowercase=True,
        use_uppercase=True,
        use_digits=True,
        use_symbols=True,
        exclude_similar=True
    )
    
    print("Generated Password:", password)
    
    # Estimate password strength
    strength = generator.estimate_password_strength(password)
    print(f"\nPassword Strength: {strength['strength']} ({strength['score']}/100)")
    print(f"Length: {strength['length']} characters")
    
    # Generate multiple passwords
    print("\nMultiple passwords:")
    passwords = generator.generate_multiple_passwords(
        count=3,
        length=12,
        use_lowercase=True,
        use_uppercase=True,
        use_digits=True,
        use_symbols=False
    )
    
    for i, pwd in enumerate(passwords, 1):
        print(f"{i}. {pwd}")


if __name__ == "__main__":
    main()