#!/bin/bash
NUM_GPUS_PER_NODE=$(nvidia-smi -L | wc -l)
WORLD_SIZE=${WORLD_SIZE:-1}
NUM_GPUS=$((NUM_GPUS_PER_NODE * WORLD_SIZE))

python -m atorch.distributed.run  --nnodes="$WORLD_SIZE" \
    --nproc_per_node="$NUM_GPUS_PER_NODE" \
    train.py --model_type llama \
    --distributed \
    --hiddien_size 64 \
    --head_num 4 \
    --layer_num 4 \
    --seq_length 32 \
    --load_strategy \
    --use_fsdp \
    --use_amp \
    --use_module_replace \
    --use_checkpointing \
    --user_created_dataloader \
    2>&1 | tee log_llama_"${WORLD_SIZE}"n"${NUM_GPUS}"g.txt 