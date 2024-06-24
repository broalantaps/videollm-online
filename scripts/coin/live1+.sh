deepspeed train.py --deepspeed configs/deepspeed/zero1.json \
    --live_version live1+ \
    --train_datasets coin_step_train coin_next_train coin_task_train coin_procedure_train coin_taskprocedure_train \
    --eval_datasets coin_step_test coin_next_test coin_task_test coin_procedure_test coin_taskprocedure_test \
    --num_train_epochs 5 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 8 \
    --gradient_checkpointing True \
    --eval_strategy no \
    --prediction_loss_only False \
    --save_strategy no \
    --learning_rate 0.0002 \
    --optim adamw_torch \
    --lr_scheduler_type cosine \
    --warmup_ratio 0.05 \
    --logging_steps 10 \
    --dataloader_num_workers 16 \
    --bf16 True \
    --tf32 True \
    --report_to tensorboard \
    --output_dir outputs/coin_benchmarks/live1+ \
