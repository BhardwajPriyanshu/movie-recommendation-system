mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $port\n\
enableCORDS = false\n\
headless = true\n\
\n\
" > ~/streamlit/config.toml