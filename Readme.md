# Secure Password Generator

A clean, secure, and highly customizable password generator built with Python. Generate cryptographically strong passwords with configurable character sets and built-in strength estimation.

## Features

- **🔒 Cryptographically Secure**: Uses Python's `secrets` module for true randomness
- **⚙️ Highly Configurable**: Customize password length and character sets
- **👁️ Avoid Ambiguity**: Option to exclude similar-looking characters (e.g., `l`, `1`, `I`, `O`)
- **📊 Strength Assessment**: Built-in password strength estimation with detailed feedback
- **🔄 Batch Generation**: Generate multiple passwords at once
- **🧹 Clean Code**: Well-structured, documented, and follows software engineering best practices
- **🔧 Flexible API**: Ready to use as a command-line tool or imported as a module

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/secure-password-generator.git
   cd secure-password-generator
   ```

2. **Ensure Python 3.6+ is installed**:
   ```bash
   python --version
   ```

No additional dependencies required! Uses only Python's standard library.

## Usage

### As a Python Module

```python
from password_generator import PasswordGenerator

# Create generator instance
generator = PasswordGenerator()

# Generate a single strong password
password = generator.generate_password(
    length=16,
    use_lowercase=True,
    use_uppercase=True,
    use_digits=True,
    use_symbols=True,
    exclude_similar=True
)

print("Generated Password:", password)

# Generate multiple passwords
passwords = generator.generate_multiple_passwords(count=5, length=12)
for i, pwd in enumerate(passwords, 1):
    print(f"Password {i}: {pwd}")

# Estimate password strength
strength = generator.estimate_password_strength(password)
print(f"Strength: {strength['strength']} ({strength['score']}/100)")
```

### Command Line Interface

Run the script directly:

```bash
python password_generator.py
```

Example output:
```
Generated Password: xK8@!pL2$qW9*rT4%

Password Strength: Very Strong (95/100)
Length: 16 characters

Multiple passwords:
1. mY7nP3kL9aB2
2. tR8qW1zX4cV6
3. jH5pL2kM8sN3
```

## API Reference

### `PasswordGenerator` Class

#### `generate_password(length=16, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True, exclude_similar=True)`
Generate a secure random password with specified parameters.

**Parameters:**
- `length`: Password length (8-128 characters, default: 16)
- `use_lowercase`: Include lowercase letters (default: True)
- `use_uppercase`: Include uppercase letters (default: True)
- `use_digits`: Include digits (default: True)
- `use_symbols`: Include symbols (default: True)
- `exclude_similar`: Exclude similar characters like 'l', '1', 'I' (default: True)

**Returns:** `str` - Generated password

**Raises:** `ValueError` if parameters are invalid

#### `generate_multiple_passwords(count=5, **kwargs)`
Generate multiple passwords with the same configuration.

**Parameters:**
- `count`: Number of passwords to generate
- `**kwargs`: Same parameters as `generate_password()`

**Returns:** `List[str]` - List of generated passwords

#### `estimate_password_strength(password)`
Estimate the strength of a password.

**Parameters:**
- `password`: Password to analyze

**Returns:** `dict` with keys:
  - `score`: Strength score (0-100)
  - `strength`: Descriptive level ("Very Weak" to "Very Strong")
  - `length`: Password length
  - `has_lowercase`, `has_uppercase`, `has_digits`, `has_symbols`: Boolean flags

## Examples

### Basic Usage
```python
# Simple 12-character password
password = generator.generate_password(length=12)
```

### Letters and Numbers Only
```python
# Password with only letters and numbers
password = generator.generate_password(
    length=14,
    use_symbols=False
)
```

### Extra Strong Password
```python
# 20-character password with all character sets
password = generator.generate_password(
    length=20,
    use_lowercase=True,
    use_uppercase=True,
    use_digits=True,
    use_symbols=True,
    exclude_similar=True
)
```

## Security Notes

- Uses `secrets` module instead of `random` for cryptographically secure random number generation
- Default password length of 16 characters provides strong security
- Excludes similar-looking characters by default to prevent confusion
- Validates all input parameters to prevent insecure configurations

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python's standard library for zero dependencies
- Inspired by best practices in password security
- Uses NIST guidelines for password strength estimation

---

**Disclaimer**: This tool is provided for educational and development purposes. Always follow your organization's security policies when generating and using passwords.
```
