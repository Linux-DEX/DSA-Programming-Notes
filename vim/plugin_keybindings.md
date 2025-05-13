# Neovim Plugin Keybindings 

## nvim-surround

### Basic Surround Actions

| Keybinding                | Description                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| `ys{motion}{char}`        | *You Surround*: Add `{char}` around the `{motion}` text             |
| `cs{target}{replacement}` | *Change Surround*: Change surrounding `{target}` to `{replacement}` |
| `ds{char}`                | *Delete Surround*: Remove surrounding `{char}`                      |

### Common Examples

| Keybinding | Result                                               |
| ---------- | ---------------------------------------------------- |
| `ysiw"`    | Surround **inner word** with quotes (`"word"`)       |
| `yss"`     | Surround **entire line** with quotes (`"line text"`) |
| `cs"'`     | Change double quotes to single quotes                |
| `ds(`      | Delete surrounding parentheses `(...)`               |
| `dss`      | Delete entire line's surrounding characters          |

### shortcut Mappings

* `b` → `()`
* `B` → `{}`

### Line Surrounding Variants

| Keybinding | Description                              |
| ---------- | ---------------------------------------- |
| `yss{`     | Surround line with `{` and `}` + spaces  |
| `yss}`     | Surround line with `{` and `}` no spaces |

### Function Call Surrounding

| Keybinding | Description                                                                 |
| ---------- | --------------------------------------------------------------------------- |
| `csf`      | Change current function call's surround                                     |
| `dsf`      | Delete current function call surround                                       |
| `ysa"f`    | Add a function call surround using `"` (e.g., `"text"` becomes `f("text")`) |

---
