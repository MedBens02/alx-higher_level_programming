#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>
#include <Python.h>
#include <string.h>
#include <unicodeobject.h>

/**
 * print_python_string - prints info about Python strings
 * @p: address of PyObject struct
 */
void print_python_string(PyObject *p)
{
	setlocale(LC_ALL, "");
	if (!p || !PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	printf("[.] string object info\n");
	printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
	printf("  length: %zd\n", PyUnicode_GET_LENGTH(p));

	const wchar_t *value = PyUnicode_AsWideCharString(p, NULL);
	if (!value)
	{
		printf("  [ERROR] Unable to read string\n");
		return;
	}

	printf("  value: %ls\n", value);
	PyMem_Free((void *)value);
}
