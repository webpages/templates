Template system for WebPages
===

This template system is very similar to **YAML** format or **Python** code, but designed to render **HTML**.

**Competitors:** [HAML](http://haml.info) ([SHPAML](https://github.com/dsc/shpaml), [PyHAML](https://github.com/mikeboers/PyHAML)), [Slim](http://slim-lang.com), [Jade](http://jade-lang.com/). Syntax is equal to [WebUI Templates](https://github.com/webui/template).


#### TODO:

- [ ] **[#2. Create parser for basic constructions](../../issues/2)**
- [x] ~~[#1. Add backend to support Django framework](../../issues/1)~~


Functions:
----

* **python-like syntax**. We don't need to close tags. Code is hierarchical and easy to read
* **extend templates**. You can assign new variable inside template and push this variable to parent template where you can use it
* **include extenstion** to support extended tags. For example, you can `include "bootstrap"` to add short syntax to generate Twiter Bootstrap markup. Instead of extra HTML tags you can write short instructions and code will be converted to correct HTML markup
