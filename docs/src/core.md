<!-- ref -->

<!-- enum -->
# EntisInitFlags

These flags determin which modules should be initialized.

## vals
ENTIS_XCB Initializes XCB connection.
ENTIS_TTF Initializes FreeType2 library.

<!-- func -->
# entis_init
bool entis_init(uint32_t width, uint32_t height, uint32_t flags);

This function must be called before all other function calls, as it constructs
the internal framebuffer, and will initialize the XCB interface, and FreeType
library is requested.

## params
[in] width This is the width of the window/framebuffer to construct.
[in] height This is the height of the window/framebuffer to construct.
[in] flags Additional initialization flags as declared by `EntisInitFlags`.

## ref
EntisInitFlags
entis_init_xcb
entis_init_ft

## return
`true` if initialization of the core module and all desired sub modules is
successful, `false` otherwise.

