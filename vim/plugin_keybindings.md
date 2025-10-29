# Neovim Plugin Keybindings

## General Keybindings

| Mode         | Key         | Command      | Description             |
| ------------ | ----------- | ------------ | ----------------------- |
| **Normal**   | `<Esc>`     | `:nohl`      | Clear search highlights |
| **Terminal** | `<Esc>`     | `<C-\><C-n>` | Exit terminal mode      |
| **Insert**   | `<C-BS>`    | `<C-w>`      | Delete previous word    |
| **Normal**   | `<leader>+` | `<C-a>`      | Increment number        |
| **Normal**   | `<leader>-` | `<C-x>`      | Decrement number        |

---

## Window Management

| Mode       | Key          | Command  | Description               |
| ---------- | ------------ | -------- | ------------------------- |
| **Normal** | `<leader>sv` | `<C-w>v` | Split window vertically   |
| **Normal** | `<leader>sh` | `<C-w>s` | Split window horizontally |
| **Normal** | `<leader>se` | `<C-w>=` | Make splits equal size    |
| **Normal** | `<leader>sx` | `:close` | Close current split       |

---

## Tab Management

| Mode       | Key          | Command     | Description                    |
| ---------- | ------------ | ----------- | ------------------------------ |
| **Normal** | `<leader>to` | `:tabnew`   | Open new tab                   |
| **Normal** | `<leader>tx` | `:tabclose` | Close current tab              |
| **Normal** | `<Tab>`      | `:tabn`     | Go to next tab                 |
| **Normal** | `<S-Tab>`    | `:tabp`     | Go to previous tab             |
| **Normal** | `<leader>tf` | `:tabnew %` | Open current buffer in new tab |

---

## Visual Mode Improvements

| Mode       | Key | Command | Description                         |
| ---------- | --- | ------- | ----------------------------------- |
| **Visual** | `<` | `<gv`   | Stay in visual mode and shift left  |
| **Visual** | `>` | `>gv`   | Stay in visual mode and shift right |

---

## Navigation Enhancements

| Mode       | Key | Command | Description                            |
| ---------- | --- | ------- | -------------------------------------- |
| **Normal** | `n` | `nzzzv` | Center search result on next match     |
| **Normal** | `N` | `Nzzzv` | Center search result on previous match |

---

## nvim-surround

### Basic Surround Actions

| Keybinding                | Description                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| `ys{motion}{char}`        | _You Surround_: Add `{char}` around the `{motion}` text             |
| `cs{target}{replacement}` | _Change Surround_: Change surrounding `{target}` to `{replacement}` |
| `ds{char}`                | _Delete Surround_: Remove surrounding `{char}`                      |

### Common Examples

| Keybinding | Result                                               |
| ---------- | ---------------------------------------------------- |
| `ysiw"`    | Surround **inner word** with quotes (`"word"`)       |
| `yss"`     | Surround **entire line** with quotes (`"line text"`) |
| `cs"'`     | Change double quotes to single quotes                |
| `ds(`      | Delete surrounding parentheses `(...)`               |
| `dss`      | Delete entire line's surrounding characters          |

### shortcut Mappings

- `b` → `()`
- `B` → `{}`

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

## nvim-tree

| Keybinding           | Command                   | Description                     |
| -------------------- | ------------------------- | ------------------------------- |
| `<leader>ee`         | `:NvimTreeToggle`         | Toggle file explorer            |
| `<leader>ec`         | `:NvimTreeCollapse`       | Collapse file explorer          |
| `<leader>er`         | `:NvimTreeRefresh`        | Refresh file explorer           |
| `<leader>eo`         | `:NvimTreeOpen`           | Open file explorer              |
| `<leader>eq`         | `:NvimTreeClose`          | Close file explorer             |
| `<leader>ef`         | `:NvimTreeFindFile`       | Find current file in explorer   |
| `<leader>ev`         | `:NvimTreeFocus`          | Focus on file explorer          |
| `<leader>en`         | `:NvimTreeResize +10`     | Increase explorer width         |
| `<leader>em`         | `:NvimTreeResize -10`     | Decrease explorer width         |
| _(optional)_ `<C-n>` | `:NvimTreeFindFileToggle` | Toggle explorer on current file |

---

## auto-session

| Keybinding   | Command           | Description                                          |
| ------------ | ----------------- | ---------------------------------------------------- |
| `<leader>wr` | `:SessionRestore` | Restore last workspace session for current directory |
| `<leader>ws` | `:SessionSave`    | Save workspace session for current working directory |

---

## formatting

| Keybinding   | Mode(s)        | Command / Action   | Description                                    |
| ------------ | -------------- | ------------------ | ---------------------------------------------- |
| `<leader>mp` | Normal, Visual | `conform.format()` | Format file or selected range (in visual mode) |

---

## gitsigns

| Keybinding   | Mode(s)          | Command / Action                          | Description                  |
| ------------ | ---------------- | ----------------------------------------- | ---------------------------- |
| `]h`         | Normal           | `gs.next_hunk`                            | Jump to next hunk            |
| `[h`         | Normal           | `gs.prev_hunk`                            | Jump to previous hunk        |
| `<leader>hs` | Normal           | `gs.stage_hunk`                           | Stage current hunk           |
| `<leader>hr` | Normal           | `gs.reset_hunk`                           | Reset current hunk           |
| `<leader>hs` | Visual           | `gs.stage_hunk({ line("."), line("v") })` | Stage selected hunk          |
| `<leader>hr` | Visual           | `gs.reset_hunk({ line("."), line("v") })` | Reset selected hunk          |
| `<leader>hS` | Normal           | `gs.stage_buffer`                         | Stage entire buffer          |
| `<leader>hR` | Normal           | `gs.reset_buffer`                         | Reset entire buffer          |
| `<leader>hu` | Normal           | `gs.undo_stage_hunk`                      | Undo stage for last hunk     |
| `<leader>hp` | Normal           | `gs.preview_hunk`                         | Preview hunk changes         |
| `<leader>hb` | Normal           | `gs.blame_line({ full = true })`          | Show full blame for line     |
| `<leader>hB` | Normal           | `gs.toggle_current_line_blame`            | Toggle inline blame display  |
| `<leader>hd` | Normal           | `gs.diffthis`                             | Diff against index           |
| `<leader>hD` | Normal           | `gs.diffthis("~")`                        | Diff against previous commit |
| `ih`         | Operator, Visual | `:<C-U>Gitsigns select_hunk<CR>`          | Select hunk as text object   |

---

## lazygit

| Keybinding   | Command    | Description     |
| ------------ | ---------- | --------------- |
| `<leader>lg` | `:LazyGit` | Open LazyGit UI |

---

## nvim lint

| Keybinding  | Mode   | Command / Action  | Description                      |
| ----------- | ------ | ----------------- | -------------------------------- |
| `<leader>l` | Normal | `lint.try_lint()` | Trigger linting for current file |

---

## noice

| Keybinding    | Mode(s)                | Command / Action                                 | Description                          |
| ------------- | ---------------------- | ------------------------------------------------ | ------------------------------------ |
| `<leader>sn`  | —                      | —                                                | Group prefix for Noice-related keys  |
| `<S-Enter>`   | Command (`c`)          | `require("noice").redirect(vim.fn.getcmdline())` | Redirect command-line input          |
| `<leader>snl` | Normal                 | `require("noice").cmd("last")`                   | Show last Noice message              |
| `<leader>snh` | Normal                 | `require("noice").cmd("history")`                | Show Noice message history           |
| `<leader>sna` | Normal                 | `require("noice").cmd("all")`                    | Show all Noice messages              |
| `<leader>snd` | Normal                 | `require("noice").cmd("dismiss")`                | Dismiss all Noice messages           |
| `<leader>snt` | Normal                 | `require("noice").cmd("pick")`                   | Open Noice picker (Telescope/FzfLua) |
| `<C-f>`       | Insert, Normal, Select | `require("noice.lsp").scroll(4)`                 | Scroll forward in Noice popup        |
| `<C-b>`       | Insert, Normal, Select | `require("noice.lsp").scroll(-4)`                | Scroll backward in Noice popup       |

---

## nvim cmp

| Keybinding  | Mode(s) | Command / Action                          | Description                           |
| ----------- | ------- | ----------------------------------------- | ------------------------------------- |
| `<S-Tab>`   | Insert  | `cmp.mapping.select_prev_item()`          | Select previous suggestion            |
| `<Tab>`     | Insert  | `cmp.mapping.select_next_item()`          | Select next suggestion                |
| `<C-b>`     | Insert  | `cmp.mapping.scroll_docs(-4)`             | Scroll documentation up               |
| `<C-f>`     | Insert  | `cmp.mapping.scroll_docs(4)`              | Scroll documentation down             |
| `<C-Space>` | Insert  | `cmp.mapping.complete()`                  | Trigger completion menu               |
| `<C-L>`     | Insert  | `cmp.mapping.complete()`                  | Trigger completion menu (alternative) |
| `<C-e>`     | Insert  | `cmp.mapping.abort()`                     | Close completion window               |
| `<CR>`      | Insert  | `cmp.mapping.confirm({ select = false })` | Confirm selected completion           |

---

## nvim treesitter text objects

### Selection Keybindings

| Keybinding | Description                                       |
| ---------- | ------------------------------------------------- |
| `a=`       | Select outer part of an assignment                |
| `i=`       | Select inner part of an assignment                |
| `l=`       | Select left-hand side of an assignment            |
| `r=`       | Select right-hand side of an assignment           |
| `a:`       | Select outer part of an object property           |
| `i:`       | Select inner part of an object property           |
| `l:`       | Select left part of an object property            |
| `r:`       | Select right part of an object property           |
| `aa`       | Select outer part of a parameter/argument         |
| `ia`       | Select inner part of a parameter/argument         |
| `ai`       | Select outer part of a conditional                |
| `ii`       | Select inner part of a conditional                |
| `al`       | Select outer part of a loop                       |
| `il`       | Select inner part of a loop                       |
| `af`       | Select outer part of a function call              |
| `if`       | Select inner part of a function call              |
| `am`       | Select outer part of a method/function definition |
| `im`       | Select inner part of a method/function definition |
| `ac`       | Select outer part of a class                      |
| `ic`       | Select inner part of a class                      |

### Swap Keybindings

| Keybinding   | Description                           |
| ------------ | ------------------------------------- |
| `<leader>na` | Swap parameter/argument with next     |
| `<leader>n:` | Swap object property with next        |
| `<leader>nm` | Swap function with next               |
| `<leader>pa` | Swap parameter/argument with previous |
| `<leader>p:` | Swap object property with previous    |
| `<leader>pm` | Swap function with previous           |

### Movement Keybindings

| Keybinding | Description                                     |
| ---------- | ----------------------------------------------- |
| `]f`       | Go to next function call start                  |
| `]F`       | Go to next function call end                    |
| `]m`       | Go to next method/function definition start     |
| `]M`       | Go to next method/function definition end       |
| `]c`       | Go to next class start                          |
| `]C`       | Go to next class end                            |
| `]i`       | Go to next conditional start                    |
| `]I`       | Go to next conditional end                      |
| `]l`       | Go to next loop start                           |
| `]L`       | Go to next loop end                             |
| `]s`       | Go to next scope (from locals.scm)              |
| `]z`       | Go to next fold (from folds.scm)                |
| `[f`       | Go to previous function call start              |
| `[F`       | Go to previous function call end                |
| `[m`       | Go to previous method/function definition start |
| `[M`       | Go to previous method/function definition end   |
| `[c`       | Go to previous class start                      |
| `[C`       | Go to previous class end                        |
| `[i`       | Go to previous conditional start                |
| `[I`       | Go to previous conditional end                  |
| `[l`       | Go to previous loop start                       |
| `[L`       | Go to previous loop end                         |

### Repeatable Movement Keybindings

| Keybinding | Description                                                |
| ---------- | ---------------------------------------------------------- |
| `;`        | Repeat last movement in the same direction                 |
| `,`        | Repeat last movement in the opposite direction             |
| `f`        | Move to next occurrence (repeatable with `;`, `,`)         |
| `F`        | Move to previous occurrence (repeatable with `;`, `,`)     |
| `t`        | Move before next occurrence (repeatable with `;`, `,`)     |
| `T`        | Move before previous occurrence (repeatable with `;`, `,`) |

---

## telescope

## Telescope Keybindings

| Keybinding    | Mode | Command / Action                      | Description                            |
| ------------- | ---- | ------------------------------------- | -------------------------------------- |
| `<leader>ff`  | n    | `Telescope find_files`                | Fuzzy find files (includes hidden)     |
| `<leader>fr`  | n    | `Telescope oldfiles`                  | Search recently opened files           |
| `<leader>fs`  | n    | `Telescope live_grep`                 | Grep text in current working directory |
| `<leader>fc`  | n    | `Telescope grep_string`               | Grep string under cursor               |
| `<leader>ft`  | n    | `TodoTelescope`                       | Search TODO comments                   |
| `<leader>fb`  | n    | `Telescope buffers`                   | Search open buffers                    |
| `<leader>/`   | n    | `Telescope current_buffer_fuzzy_find` | Search text within current buffer      |
| `<leader>fk`  | n    | `Telescope keymaps`                   | Search keymaps                         |
| `<leader>fh`  | n    | `Telescope help_tags`                 | Search help documentation              |
| `<leader>fgb` | n    | `Telescope git_branches`              | Search Git branches                    |

### Inside Telescope Prompt (Insert Mode)

| Keybinding            | Action                                                                  |
| --------------------- | ----------------------------------------------------------------------- |
| `<C-j>`               | Move to next item                                                       |
| `<C-k>`               | Move to previous item                                                   |
| `<C-q>`               | Send selected items to quickfix + open with Trouble                     |
| `<C-t>`               | Open with Trouble Telescope integration                                 |
| `<C-Space>` / `<C-L>` | Trigger completion suggestions                                          |
| `<C-e>`               | Abort / close Telescope                                                 |
| `<CR>`                | Open file in a new tab (`tab drop`) or switch to buffer if already open |

---

## todo comments

| Keybinding | Mode   | Action                      | Description                       |
| ---------- | ------ | --------------------------- | --------------------------------- |
| `]t`       | Normal | `todo_comments.jump_next()` | Jump to **next** TODO comment     |
| `[t`       | Normal | `todo_comments.jump_prev()` | Jump to **previous** TODO comment |

---

## toggleterm

| Mode         | Key          | Action                | Description                 |
| ------------ | ------------ | --------------------- | --------------------------- |
| **Normal**   | `<A-i>`      | `float_term:toggle()` | Toggle floating terminal    |
| **Normal**   | `<leader>th` | `horiz_term:toggle()` | Toggle horizontal terminal  |
| **Normal**   | `<leader>tv` | `vert_term:toggle()`  | Toggle vertical terminal    |
| **Terminal** | `<Esc>`      | `<C-\><C-n>`          | Exit terminal mode          |
| **Terminal** | `<A-h>`      | `<C-\><C-n><C-w>h`    | Move to window on the left  |
| **Terminal** | `<A-j>`      | `<C-\><C-n><C-w>j`    | Move to window below        |
| **Terminal** | `<A-k>`      | `<C-\><C-n><C-w>k`    | Move to window above        |
| **Terminal** | `<A-l>`      | `<C-\><C-n><C-w>l`    | Move to window on the right |

---

## trouble

| Mode       | Key          | Command                                    | Description                |
| ---------- | ------------ | ------------------------------------------ | -------------------------- |
| **Normal** | `<leader>xw` | `:Trouble diagnostics toggle`              | Open workspace diagnostics |
| **Normal** | `<leader>xd` | `:Trouble diagnostics toggle filter.buf=0` | Open document diagnostics  |
| **Normal** | `<leader>xq` | `:Trouble quickfix toggle`                 | Open quickfix list         |
| **Normal** | `<leader>xl` | `:Trouble loclist toggle`                  | Open location list         |
| **Normal** | `<leader>xt` | `:Trouble todo toggle`                     | Open todos in Trouble      |

---

## vim-maximizer

| Mode       | Key          | Command            | Description               |
| ---------- | ------------ | ------------------ | ------------------------- |
| **Normal** | `<leader>sm` | `:MaximizerToggle` | Maximize/minimize a split |

---
