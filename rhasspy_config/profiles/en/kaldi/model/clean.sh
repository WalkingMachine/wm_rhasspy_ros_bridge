#!/usr/bin/env bash
this_dir="$( cd "$( dirname "$0" )" && pwd )"

cd "${this_dir}" && \
    rm -rf \
       ../dictionary.txt ../language_model.txt unknown_words.txt

cd "${this_dir}" && \
    rm -rf \
       data/ graph/HCLG.fst online/ run/ utils
