#include <stdlib.h>
#include <Python.h>
#include <stdio.h>


void print_python_list(PyObject *p)
{
    Py_ssize_t i, j;
    PyObject *item;

    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < PyList_Size(p); i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item)) {
            printf("  [ERROR] Invalid Bytes Object\n");
            return;
        }
        if (PyList_Check(item)) {
            print_python_list(item);
        }
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size;
    unsigned char *bytes;

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    size = PyBytes_Size(p);
    if (size > 10) {
        size = 10;
    }

    bytes = (unsigned char *)PyBytes_AsString(p);
    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++) {
        printf("%02x", bytes[i]);
        if (i == size - 1) {
            printf("\n");
        } else {
            printf(" ");
        }
    }
}
