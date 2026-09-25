#include <Python.h>

static PyObject* fastpy_add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(a + b);
}

static PyObject* fastpy_mul_double(PyObject* self, PyObject* args) {
    double x, y;
    if (!PyArg_ParseTuple(args, "dd", &x, &y)) {
        return NULL;
    }
    return PyFloat_FromDouble(x * y);
}

static PyMethodDef FastCoreMethods[] = {
    {"add", fastpy_add, METH_VARARGS, "Add two integers"},
    {"mul_double", fastpy_mul_double, METH_VARARGS, "Multiply two floating-point numbers"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fastcoremodule = {
    PyModuleDef_HEAD_INIT,
    "fastcore",
    "fastpy high-performance core module",
    -1,
    FastCoreMethods
};

PyMODINIT_FUNC PyInit_fastcore(void) {
    return PyModule_Create(&fastcoremodule);
}6
