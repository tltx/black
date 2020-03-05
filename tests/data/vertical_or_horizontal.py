def foo():
    return render(request, template_name="i", context=context,)

nested = {
    (1, 2, 3),
    (4, 5, 6),
}
foo(
    last_page,
    rows,
    page,
    False,
)
def spaces_types(
    a: int = 1,
    b: tuple = (),
    c: list = [],
    d: dict = {},
    e: bool = True,
    f: int = -1,
    g: int = 1 if False else 2,
):
    ...
# output
def foo():
    return render(
        request,
        template_name="i",
        context=context,
    )


nested = {
    (1, 2, 3),
    (4, 5, 6),
}
foo(
    last_page,
    rows,
    page,
    False,
)


def spaces_types(
    a: int = 1,
    b: tuple = (),
    c: list = [],
    d: dict = {},
    e: bool = True,
    f: int = -1,
    g: int = 1 if False else 2,
):
    ...
