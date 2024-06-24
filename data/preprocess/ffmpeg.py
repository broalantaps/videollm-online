from functools import partial
import submitit, transformers
from dataclasses import dataclass

from models.arguments_live import LiveOnePlusTrainingArguments
from ..utils import distributed_ffmpeg

@dataclass
class LiveOnePlusEncodingArguments(LiveOnePlusTrainingArguments):
    num_nodes: int = 1
    num_gpus: int = 8
    video_dir: str = 'datasets/ego4d/v2/full_scale'
    slurm_partition: str = None
    
if __name__ == "__main__":
    args, = transformers.HfArgumentParser(LiveOnePlusEncodingArguments).parse_args_into_dataclasses()
    executor = submitit.AutoExecutor(folder=f"outputs/preprocess/")
    task = partial(distributed_ffmpeg, src_root=args.video_dir, resolution=args.frame_resolution, fps=args.frame_fps)
    executor.update_parameters(
        tasks_per_node=args.num_gpus,
        nodes=args.num_nodes,
        gpus_per_node=args.num_gpus,
        slurm_partition=args.slurm_partition,
        cpus_per_task=10,
        mem_gb=240,
        slurm_time='24:00:00',
    )
    job = executor.submit(task)