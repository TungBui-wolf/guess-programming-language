import traceback

import streamlit as st
from model import guess_programming_language, load_model

DEFAULT_MODEL_DIR = "my_model/"
classiffer = load_model(DEFAULT_MODEL_DIR)

def guess(code):
    if not code or len(code) <= 20:
        return "<h4 style=\"color: red;font-weight: bold;\">Please type more than 20 characters!</h4><br>"
    language, score = guess_programming_language(classiffer, code)
    return "<h4 style=\"color: red;font-weight: bold;\">{} ({} %)</h4><br>".format(language, score)


if __name__ == '__main__':
    st.title('Programming Language Detection Demo')
    st.info("Detect programming language from source code")

    code = st.text_area('Just paste your code here: ')

    submit = st.button("Submit")
    st.header("Predict result:")

    html = "<h4 style=\"color: red;font-weight: bold;\">Result Here</h4><br>"
    results = st.markdown(html, unsafe_allow_html=True)

    reset = st.button("RESET")

    st.text("List of supported programming languages:")
    st.info("Total 53 programming language, example: Python, Java, C#, C++, C, HTML, Objective-C, Haskell, Rust, Matlab, Nix, Swift, Go, Protobuf, Lua, Pascal, Lisp, Wasm, Q, Actions Script, Haxe, Handlebars, Dart, Live Script, Json ...")

    if submit:
        results.empty()
        results.markdown(guess(code), unsafe_allow_html=True)
    if reset:
        results.empty()
        results.markdown(html, unsafe_allow_html=True)
