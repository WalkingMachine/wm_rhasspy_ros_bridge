#!/usr/bin/env bash

# Need to make all paths absolute
kaldi_dir="$(realpath "$1")"
model_dir="$(realpath "$2")"
graph_dir="$(realpath "$3")"
wav_path="$(realpath "$4")"

# Required bin/lib directories
lib_dir="${kaldi_dir}/src/lib"
openfst_dir="${kaldi_dir}/tools/openfst"
utils_dir="${kaldi_dir}/egs/wsj/s5/utils"
steps_dir="${kaldi_dir}/egs/wsj/s5/steps"

# Create a symbolic link to the "utils" directory.
# Some Kaldi scripts will crash without this.
if [[ ! -e "${model_dir}/utils" ]]; then
    ln -fs "${utils_dir}" "${model_dir}/utils"
fi

# Set up paths for Kaldi programs
export PATH="${kaldi_dir}/src/featbin:${kaldi_dir}/src/latbin:${kaldi_dir}/src/gmmbin:${kaldi_dir}/src/online2bin:$PATH"
export LD_LIBRARY_PATH="${lib_dir}:${openfst_dir}/lib:${LD_LIBRARY_PATH}"

# -----------------------------------------------------------------------------
# WAV files
# -----------------------------------------------------------------------------

# Create temporary directory and clean it up when script finishes
temp_dir="$(mktemp -d)"
function finish {
    rm -rf "${temp_dir}"
}

trap finish EXIT

# -----------------------------------------------------------------------------

# Mapping from WAV name (key) to its individual real-time duration.
# Used to estimate decoding time.
declare -A wav_durations

# Write spk2utt and wav.scp files
wav_name="$(basename "${wav_path}")"
echo "utt_1 ${wav_path}" > "${temp_dir}/wav.scp"

# Assume from a single speaker
echo "corpus utt_1" > "${temp_dir}/spk2utt"

# -----------------------------------------------------------------------------
# Decode
# -----------------------------------------------------------------------------

online_dir="${model_dir}/online"
online2-wav-nnet3-latgen-faster \
    --online=false \
    --do-endpointing=false \
    --frame-subsampling-factor=3 \
    "--config=${online_dir}/conf/online.conf" \
    --max-active=7000 \
    --beam=15.0 \
    --lattice-beam=6.0 \
    --acoustic-scale=1.0 \
    "--word-symbol-table=${graph_dir}/words.txt" \
    "${model_dir}/model/final.mdl" \
    "${graph_dir}/HCLG.fst" \
    "ark:${temp_dir}/spk2utt" \
    "scp:${temp_dir}/wav.scp" \
    'ark:/dev/null' \
    2>&1 | \
    grep '^utt_1' | \
    sed -e 's/^utt_1//'
