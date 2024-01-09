#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - Prints information about a Python list.
 * @p: Pointer to the Python list.
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *python_list = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", python_list->allocated);

	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(python_list->ob_item[i])->tp_name);
}
