#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Python bytes object
 * Return: No return value
 */
void print_python_bytes(PyObject *p)
{
    char *byte_str;
    long int size, i;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    byte_str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", byte_str);
    printf("  first %ld bytes:", (size <= 10) ? size : 10);

    for (i = 0; i < 10 && i < size + 1; i++)
    {
        if (byte_str[i] >= 0)
        	printf(" %02x", byte_str[i]);
        else
        	printf(" %02x", byte_str[i] + 256);
    }
    printf("\n");
}

/**
 * print_python_list - Prints information about a Python list
 * @p: Python list object
 * Return: No return value
 */
void print_python_list(PyObject *p)
{
    long int list_size, i;
    PyListObject *list;
    PyObject *elt;

    list_size = ((PyVarObject *)p)->ob_size;
    list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", list_size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < list_size; i++)
	{
		elt = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((elt)->ob_type)->tp_name);
		if (PyBytes_Check(elt))
			print_python_bytes(elt);
	}
}
