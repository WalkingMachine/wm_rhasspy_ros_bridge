#!/usr/bin/env bash

# Need to make all paths absolute
kaldi_dir="$(realpath "$1")"
model_dir="$(realpath "$2")"
dict_file="$(realpath "$3")"
lm_file="$(realpath "$4")"

graph_dir="${model_dir}/graph"

steps_dir="${kaldi_dir}/egs/wsj/s5/steps"
utils_dir="${kaldi_dir}/egs/wsj/s5/utils"
bin_dir="${kaldi_dir}/src/bin"
lib_dir="${kaldi_dir}/src/lib"
fstbin_dir="${kaldi_dir}/src/fstbin"
lmbin_dir="${kaldi_dir}/src/lmbin"
openfst_dir="${kaldi_dir}/tools/openfst"

# Empty path.sh
touch "${model_dir}/path.sh"

# Force create a symbolic link to the "utils" directory.
# Some Kaldi scripts will crash without this.
rm -rf "${model_dir}/utils"
ln -fs "${utils_dir}" "${model_dir}/utils"

export PATH="${utils_dir}:${fstbin_dir}:${lmbin_dir}:${bin_dir}:${openfst_dir}/bin:$PATH"
export LD_LIBRARY_PATH="${lib_dir}:${openfst_dir}/lib:${LD_LIBRARY_PATH}"

# Clean up
echo "Cleaning up"
rm -rf "${model_dir}/data"
rm -rf "${graph_dir}"

# Lexicon
echo "Generating lexicon"
mkdir -p "${model_dir}/data/local/dict"
cp "${model_dir}"/phones/*.txt "${model_dir}/data/local/dict/"
cp "${dict_file}" "${model_dir}/data/local/dict/lexicon.txt"
cd "${model_dir}" && \
    "${utils_dir}/prepare_lang.sh" \
        "${model_dir}/data/local/dict" '' \
        "${model_dir}/data/local/lang" "${model_dir}/data/lang"

# Language model
echo "Formatting language model"
cat "${lm_file}" | gzip --to-stdout > "${model_dir}/data/local/lang/lm.arpa.gz"
cd "${model_dir}" && \
    "${utils_dir}/format_lm.sh" \
        "${model_dir}/data/lang" "${model_dir}/data/local/lang/lm.arpa.gz" \
        "${model_dir}/data/local/dict/lexicon.txt" "${model_dir}/data/lang"

# Graph
echo "Creating graph"
cd "${model_dir}" && \
    "${utils_dir}/mkgraph.sh" \
        "${model_dir}/data/lang" \
        "${model_dir}/model" \
        "${graph_dir}"

# Prepare online configuration
echo "Preparing online decoding"
online_dir="${model_dir}/online"
cd "${model_dir}" && \
    "${steps_dir}/online/nnet3/prepare_online_decoding.sh" \
        --mfcc-config "${model_dir}/conf/mfcc_hires.conf" \
        "${model_dir}/data/lang" \
        "${model_dir}/extractor" \
        "${model_dir}/model" \
        "${online_dir}"

echo "Training succeeded"
