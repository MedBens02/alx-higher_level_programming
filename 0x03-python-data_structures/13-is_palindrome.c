#include "lists.h"

/**
 * is_palindrome - Checks if str is a palindrome.
 * @s: str.
 * @l: length of the string.
 * Return: 1 if str is a palindrome, 0 otherwise.
 */
int is_palindrome(char *s)
{
	int l = _strlen(s);

	return (palindrome(s, l));
}

/**
 * _strlen - returns the length of a str.
 *
 * @s: str.
 *
 * Return: length of str.
 */
int _strlen(char *s)
{
	if (*s != '\0')
		return (_strlen(s + 1) + 1);

	return (0);
}

/**
 * palindrome - check palindrome.
 * @s: str to check.
 * @l: length of the str.
 * Return: 1 if str is a palindrome, 0 otherwise.
 */
int palindrome(char *s, int l)
{
	if (l <= 1)
		return (1);

	else if (*s == s[l - 1])
		return (palindrome(s + 1, l - 2));

	return (0);
}
