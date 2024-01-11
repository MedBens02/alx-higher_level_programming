#include <stdio.h>
#include <Python.h>
#include <stdlib.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *byte_str;
	unsigned int size, i;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	
	size = ((PyVarObject *)p)->ob_size
	byte_str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", byte_str);

	(size >= 10) ? size = 10 : size += 1;

	printf("  first %ld bytes: ", size);

	for (i = 0; i < size; i++)
	{ 
		printf("%02hhx", byte_str[i]);
		if (i == (size - 1)
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_list - Prints information about a Python list
 * @p: Python list object
 */
void print_python_list(PyObject *p)
{
	int list_size, i;
	PyListObject *list;
	const char *elt_type;

	list_size = ((PyVarObject *)p)->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", list->allocated);

	for (i = 0; i < list_size; i++)
	{
		elt_type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, elt_type);
		if (strcmp(elt_type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
