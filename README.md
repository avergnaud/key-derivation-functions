https://stackoverflow.com/questions/549/the-definitive-guide-to-form-based-website-authentication

"So if you can't store the password, how do you check that the login+password combination POSTed from the login form is correct? The answer is hashing using a key derivation function. Whenever a new user is created or a password is changed, you take the password and run it through a KDF, such as Argon2, bcrypt, scrypt or PBKDF2, turning the cleartext password ("correcthorsebatterystaple") into a long, random-looking string, which is a lot safer to store in your database"

https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/