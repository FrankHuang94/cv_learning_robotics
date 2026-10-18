"""Simplified Chinese translations of kb_recent.RECENT_UPDATES, entries [19:35].

Covers compute/latency/deployment, perception foundations, core robotics CV
problems, 3D and spatial understanding, multimodal perception, and
self-supervised robot perception.
"""

RECENT_UPDATES_ZH_C = {
    "09_robot_platforms_and_hardware/05_compute_latency_and_deployment": """
**机载算力。** NVIDIA 的 Jetson AGX Thor（Blackwell GPU，128 GB 内存）于 2025 年 8 月 25 日正式全面上市，开发者套件售价 $3,499。它现已成为众多人形机器人的默认机载计算机，GR00T 参考设计也采用了它。

**成本。** 据行业媒体报道，2026 年 7 月 NVIDIA 在未事先公告的情况下将 Jetson 价格最多上调约 100%；Thor 开发者套件涨至 $5,499。相关报道将涨价归因于内存成本。因此，边缘算力是物料清单（BOM）和科研预算中的一项重要因素，而非价格持续下降的大宗商品。

**模型侧对延迟的应对**

- **端侧 VLA：** Gemini Robotics On-Device（2025 年 6 月）与 On-Device 2（2026 年 7 月）。
- **紧凑模型：** SmolVLA（450M）与 X-VLA（0.9B）。
- **异步执行：** Real-Time Chunking（实时分块）。
- **显式的频率分层：** Helix 02 中 S0 以 1 kHz、S1 以 200 Hz 运行，S2 运行频率更低。
- **非实时层采用托管推理：** Physical Intelligence 的 API 测试版（2026 年 10 月）。

**应当报告什么。** 部署类论文应说明哪些层在机载端运行、哪些层在机外运行，以及各层的尾部延迟。
""",
    "02_robot_perception_foundations/02_camera_models_calibration": """
**标定成为一种可学习的输入**

前馈式几何模型现在可以与深度一起联合估计内参和位姿，并在已知标定可用时接收它作为输入：

- VGGT（CVPR 2025 最佳论文）；
- MapAnything（3DV 2026），可接收可选的内参、位姿或深度；
- Depth Anything 3（2025 年 11 月），可从任意数量的视图预测深度、位姿和内参。

因此，标定正在从硬性前提转变为一种软性输入。

**相机几何作为策略输入**

在策略方面，ICRA 2026 机器人学习最佳论文“Do You Know Where Your Camera Is? View-Invariant Policy Learning with Camera Conditioning”将模仿学习策略以相机外参为条件。显式的相机几何提升了所学策略对视角变化的鲁棒性。

**启示**

标定质量已成为需要报告和施加扰动的变量，而不是可以略去不提的准备步骤。
""",
    "02_robot_perception_foundations/03_depth_stereo_rgbd": """
**面向双目与深度的基础模型**

- **FoundationStereo**（NVIDIA，CVPR 2025）：零样本双目立体匹配，训练数据为约一百万对精选合成图像对。
- **Fast-FoundationStereo**（arXiv 2512.11130，CVPR 2026）：通过蒸馏、架构搜索和剪枝，在精度相近的情况下速度提升十倍以上。
- **Depth Anything 3**（ByteDance Seed，2025 年 11 月）：用一个朴素的 transformer 从任意数量的视图预测一致的深度和相机射线。
- **MapAnything：** 可由图像与可选几何输入的灵活组合生成度量尺度重建。

**对机器人的启示**

- 对于配备双目相机头的机器人，在许多室内场景中，学习式双目已成为替代主动深度传感器的现实选择。
- 在透明、反光和无纹理表面上的失效行为，仍须在机器人自身的数据上加以测量。
- 各检查点（checkpoint）的许可证不尽相同。
""",
    "03_core_robotics_cv_problems/01_object_detection_for_robotics": """
**开放词汇检测与分割已整合到少数几个基础模型中。**

- **SAM 3 “Segment Anything with Concepts”**（Meta，2025 年 11 月，ICLR 2026）
  - 在图像和视频中返回与某个名词短语或图像示例相匹配的所有实例。
  - 提出了包含约 270,000 个概念的 SA-Co 基准。
  - 在很大程度上取代了 Grounded-SAM 式“检测器加分割器”的流水线。
- **DINOv3**（Meta，2025 年 8 月）：一个 7B 自监督骨干网络（另有蒸馏版本），其冻结特征在稠密任务上可与专用模型相媲美。
- **SigLIP 2**（2025 年 2 月）。
- **Meta 的 Perception Encoder**（2025 年 4 月）。

**对机器人领域意味着什么**

- 检测瓶颈进一步向下游转移，落在：
  - 度量位姿；
  - 操作过程中的实例持续性；
  - 对不存在物体的校准拒识。
- 概念提示很容易“找到”一个实际并不存在的物体。评测应包含负例查询。
""",
    "03_core_robotics_cv_problems/02_pose_estimation_and_6d_pose": """
**截至 2026 年 10 月，FoundationPose 尚未出现被广泛采用的继任者。** 基于模型的新物体位姿估计与跟踪仍是参考方法。

**相关进展**

- **SAM 3D Objects**（Meta，2025 年 11 月；CVPR 2026 荣誉提名）可从单张图像重建物体和场景。这使得无需预先网格的流水线成为可能：在位姿估计之前即时生成物体模型。
- **前馈式多视图几何**（VGGT、MapAnything）提供相机位姿和点图（point map），可用于初始化物体位姿。
- **事件相机 6D 位姿（MTevent，CVPR 2025 研讨会）：** 基于 RGB 的 FoundationPose 在其高速序列上得分极低。这揭示了基于帧的位姿方法在运动模糊和高动态范围方面尚未弥合的差距。
""",
    "03_core_robotics_cv_problems/07_egocentric_perception": """
**第一人称人类数据已成为机器人学习的主流资源。**

- **EgoDex**（Apple，ICLR 2026）：829 小时的 Vision Pro 第一人称视频，带 3D 手部跟踪，覆盖 194 个任务。
- **EgoMimic**（ICRA 2025）和 **EgoZero** 从 Project Aria 录制数据中学习操作。Meta 的 Aria Gen 2 眼镜已于 2026 年交付研究用户。
- **2026 年更大规模的语料：** EgoVerse 与 EgoLive 各自报告的数据量超过一千小时。

**产业应用**

- Physical Intelligence 报告称，在经过充分预训练的 VLA 中会涌现出人到机器人的迁移能力（2025 年 12 月）。
- Figure 的 Project Go-Big 利用人类视频训练导航。
- 1X 利用第一人称视频素材对其世界模型进行适配。

**具身形态差距仍是关键的研究变量**

这一差距涵盖手部形态、相机安装位置以及力标签的缺失。所报告的增益应按事后追加了多少机器人数据进行分层呈现。
""",
    "04_3d_and_spatial_understanding/00_overview": """
**前馈式几何已成为面向机器人的 3D 视觉中的主导趋势。**

如今，单个网络即可在数秒内从一张到数百张图像中推断出相机、深度、点图和轨迹：

- **VGGT：** CVPR 2025 最佳论文。
- **CUT3R：** 具有持久状态的循环模型。
- **π³：** 具有置换等变性，因此结果不依赖于输入顺序。
- **MapAnything。**
- **Depth Anything 3。**
- **VGGT-Ω**（CVPR 2026）。

**从静态场景到动态场景。** D4RT（CVPR 2026 最佳论文）将这一思路扩展到动态 4D 重建，其查询解码器可回答任意时刻任意点的查询。

**机器人获得了什么，哪些问题仍未解决**

- 这些模型为机器人提供了无需逐场景优化的快速空间前端。
- 度量尺度、不确定性以及机器人交互后的在线更新仍是未解决的问题。
""",
    "04_3d_and_spatial_understanding/02_sfm_slam_and_visual_odometry": """
**学习式重建先验已直接进入 SLAM**

- **MASt3R-SLAM**（CVPR 2025）：在 MASt3R 先验之上实现约 15 FPS 的实时单目稠密 SLAM。它不假设参数化相机模型，并加入了回环检测与全局优化。
- **CUT3R**（CVPR 2025）：维护一个持久的循环状态，可针对静态和动态场景在线输出度量点图。
- **VGGT** 与 **π³** 通过单次前馈即可给出相机估计，对于短序列可用于初始化或替代经典的运动恢复结构（SfM）。
- **2026 年的流式变体：** 一波预印本瞄准长序列和里程计，但目前仍仅见于 arXiv。

**机器人领域的开放问题**

长时程漂移、重定位以及场景变化下的地图维护，仍然更适合采用具有显式优化后端的系统。基准应同时报告长轨迹上的精度和失效频率。
""",
    "04_3d_and_spatial_understanding/04_3d_gaussian_splatting_for_robotics": """
**高斯泼溅正朝着前馈式构建和仿真用途发展。**

- **AnySplat**（2025 年年中）可一次性从无位姿、未标定的视图预测 3D 高斯场景。
- 据 Isaac Sim 6.0 的相关报道，**NVIDIA** 已将基于高斯的神经重建集成到 Isaac Sim 中，用于构建仿真场景。
- **EmbodiedSplat**（ICCV 2025）利用手机拍摄的泼溅表示实现“现实到仿真再到现实”的导航。
- **基于泼溅构建的软体数字孪生**（arXiv 2511.04665）得到的仿真策略成功率与真实成功率的相关系数达到 0.897 或更高。

**上文的警示依然成立。** 光度保真并不意味着几何上可安全用于碰撞检测，也不意味着接触动力学正确。
""",
    "04_3d_and_spatial_understanding/05_dynamic_4d_scene_understanding": """
**基于单目视频的动态 4D 重建已变得快速且前馈化。**

- **D4RT**（Google DeepMind、UCL 与 Oxford；CVPR 2026 最佳论文）采用全局编码器和查询解码器。它可回答任意时刻任意点的几何与运动，据报道比先前方法快 18–300 倍。
- **MegaSaM**（CVPR 2025 荣誉提名）可从随手拍摄的动态视频中恢复相机和深度。
- **SpatialTrackerV2**（ICCV 2025）执行前馈式 3D 点跟踪，并联合估计深度与位姿。
- **CUT3R** 可在线处理动态场景。

**在操作中的应用。** 这些模型使得在操作过程中跟踪形变物体和铰接物体变得可行。但针对机械臂遮挡、并在满足控制需求的延迟下进行的机器人专项评测仍然稀缺。
""",
    "04_3d_and_spatial_understanding/07_spatial_reasoning_bottlenecks": """
**新基准使瓶颈变得可测量**

- **VSI-Bench**（“Thinking in Space”，CVPR 2025）：包含 5,000 多个视频空间问题。研究发现，显式认知地图可提升多模态 LLM 的距离推理能力。
- **Cambrian-S 与 VSI-SUPER**（2025 年 11 月）：将其扩展到长时程空间“超感知”（supersensing）。
- **Google DeepMind 的 ERQA：** 400 道具身推理问题。

**为具身空间推理而训练的模型**

- Gemini Robotics-ER 1.5、1.6 和 2。
- BAAI 的 RoboBrain 2.0。
- NVIDIA 的 Cosmos Reason 系列。

这些模型报告在此类基准上取得了大幅提升。

**这些基准仍遗漏了什么**

这些基准仍以问答为主。上文的核心批评依然成立：很少有评测通过可达性或实际执行的操作来验证空间问题的答案。
""",
    "05_multimodal_perception/02_visuotactile_learning": """
**触觉感知正从研究平台走向产品和基础模型。**

- **表征学习**
  - Meta 的 Sparsh：自监督触觉表征。
  - Digit 360：一款多模态指尖传感器，于 2024 年底与 GelSight 和 Wonik 联合发布。
  - Sparsh-X（2025 年 6 月）融合来自 Digit 360 的图像、音频、惯性和压力信号。其作者报告策略成功率大幅提升。
- **商用硬件与模型**
  - Figure 03 增加了触觉指尖。
  - Amazon 的 Vulcan 上架与拣选机器人（2025 年 5 月）在生产中使用力觉和触觉感知。
  - Microsoft 的 Rho-alpha（2026 年 1 月）在 VLA 内部通过一个专用的动作专家来处理触觉输入。
- **规模化预印本：** 2026 年出现了一批关于视触觉规模化的预印本，包括视觉-触觉-语言-动作模型和触觉世界模型。目前尚无一项成为标准基线。
""",
    "05_multimodal_perception/03_language_grounded_perception": """
**语言定位（grounding）已变为概念级且可提示。** SAM 3（2025 年 11 月）可在视频中分割并跟踪某个名词短语或示例的所有实例。

**具身推理模型会输出经过定位的中间量。** 这些中间量包括点、框、轨迹和成功判断：

- Gemini Robotics-ER 1.5、1.6 和 2；
- Cosmos Reason 2；
- RoboBrain 2.0；
- MolmoAct。

**面向机器人的注意事项**

- 定位结果必须在机器人坐标系中并随时间加以验证。
- 模型自身给出的成功判断必须与独立的结果检测器进行核对。
""",
    "05_multimodal_perception/04_open_vocabulary_robot_perception": """
**2026 年的开放词汇技术栈**

- **骨干网络：**
  - DINOv3，用于稠密自监督特征；
  - SigLIP 2 或 Perception Encoder，用于语言对齐特征。
- **概念分割与跟踪：** SAM 3。
- **单图像物体与场景重建：** SAM 3D。
- **3D 提升：** 前馈式几何（VGGT、MapAnything）。

**瓶颈如今所在**

- 识别广度已不再是瓶颈。
- 瓶颈在于：
  - 将概念与可供性和可达性关联起来；
  - 在操作过程中保持物体身份；
  - 拒绝针对不存在物体的查询。

**OVMM 式评测** 仍是恰当的检验方式，因为它将语义搜索与物理拾取联系在一起。
""",
    "05_multimodal_perception/06_event_cameras_and_high_speed_vision": """
**事件视觉开始与基础模型交汇**

- **新基准：** EventBench（arXiv 2511.18448），用于在事件流上评测多模态模型。
- **数据集：** MTevent 6D 位姿数据集，基于帧的 FoundationPose 在其上表现不佳。
- **预印本：** 2026 年提出以事件为条件的 VLA 的工作，以及若干表征综述。

**仍然缺失的部分。** 主流机器人基础模型仍是基于帧的。上文列出的开放问题没有变化：事件词元化、大规模预训练以及低功耗部署。
""",
    "07_data_simulation_and_training/07_self_supervised_robot_perception": """
**自监督视觉预训练达到新的规模**

- **DINOv3**（2025 年 8 月）：在 1.7B 张图像上训练的 7B ViT。
- **V-JEPA 2**（2025 年 6 月）：视频自监督学习模型，在使用少量机器人视频后还可支持以动作为条件的规划。
- **RoboJEPA**（2026 年 10 月）：将隐变量预测扩展到 12 种具身形态，并呈现幂律规律。

**共同的经验。** 自监督特征能很好地迁移到机器人感知。但可执行的能力仍需要带动作标签的数据或交互。
""",
}
