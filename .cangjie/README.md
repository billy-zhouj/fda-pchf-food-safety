# `.cangjie/` — 构建脚本与权威链（2026-11-10，v4.19 双血缘收口）

> **一句话**：`build_v4.19.py` 是**唯一全量构建入口**；`install_v18.py` 是**唯一安装入口**；
> 旧链已整体冻结进 `_legacy/old-chain-v416/`，脚本带 DEPRECATED 守卫（默认 `exit 2`）。

## 1. 权威链（唯一）

```
build/v4.16-baseline/           v4.16 基线（dist-v20 33 文件 + 根 test-prompts.json 168 用例）
        │
        ├── build/v4.19/v4.17/capabilities/   11 张卡（IOM Ch.6：入口 + imports/ 10）
        ├── build/v4.19/v4.18/capabilities/    6 张卡（Part 101：入口 + labeling/ 5）
        ├── build/v4.19/v4.19/capabilities/    6 张卡（Part 172：入口 + additives/ 5）
        └── build/v4.19/final/                 6 个终态文件（SKILL.md / test-prompts.json /
                                                capability-index / cheatsheet / glossary / overview）
        │
   .cangjie/build_v4.19.py   （铺基线 34 → 叠加 23 卡 → 覆盖 6 终态 → 57 文件 sha256 全等 dist-v21）
        │
   dist-v21/                 v4.19 参考产物（57 文件，权威）
        │
   .cangjie/install_v18.py   （备份 → 整目录镜像 → 官方校验 → sha256 比对）
        │
   ~/.workbuddy/skills/fda-pchf-food-safety   （用户级已装技能）
```

**验证方式**：`python .cangjie/build_v4.19.py` → 必须输出 `[4] 与 dist-v21 对齐：57 文件 sha256 全部一致`
且 `[5] version 4.19 / 能力卡 51 文件 / 术语 318 / 用例 204`。任一不符即构建失败（脚本内 assert）。

## 2. 为什么是「冻结增量」而不是重跑 apply 脚本

| 版本 | apply 脚本可重放性 | 结论 |
|---|---|---|
| v4.17 | 依赖原 book 的 `dist/`（归档未收）＋路径硬编码原开发机 | 不可 |
| v4.18 | 依赖 book 相对路径 `ROOT/candidates/glossary.md`，SKILL 路径硬编码 | 不可 |
| v4.19 | **原 book 无 apply 脚本**（交互式手工完成，从未脚本化） | 不可 |

因此把「当时实际写入的内容」固化为 `build/v4.19/` 下的**不可变输入**（生成时逐文件断言与
dist-v21 对应文件 sha256 相等）。构建因此确定性、零外部依赖、可在任何机器复现。

## 3. 三件套职责

| 文件 | 职责 | 何时改 |
|---|---|---|
| `build_v4.19.py` | 全量构建 → dist-v21 等价产物 + 全量断言 | 只在新增版本时新建 `build_vX.py`，不改本文件 |
| `install_v18.py` | 把 `dist-v21` 装到用户级技能目录（备份/镜像/校验） | 同上，新版本新建 `install_vX.py` |
| `README.md` | 本索引 + 权威决议 + 目录地图 | 结构变化时同步 |

## 4. 规则（硬性）

1. **构建只走 `build_v4.19.py`**，安装只走 `install_v18.py`。出新版：新建 `build_vX.py` / `install_vX.py`，
   旧脚本加守卫、不改其内容。
2. **禁止**执行 `_legacy/old-chain-v416/scripts/` 下任何脚本（旧链，默认 `exit 2`；
   仅路线 A 研究可 `export ALLOW_DEPRECATED_CANGJIE=1` 放行）。
3. 任何脚本改动后：`python -c "import ast; ast.parse(open(...))"` → 构建到临时目录验证 → 再跑正式目标。
4. `build/` 与 `dist-v21/` 是**输入/参考产物**，不得在构建时被修改；产物只写到临时目录。

## 5. 目录地图

```
仓库根/
├── build/                      ★ 构建输入（权威）
│   ├── v4.16-baseline/         v4.16 基线（33 文件 + test-prompts.json）
│   └── v4.19/                  v4.19 冻结增量（v4.17/ v4.18/ v4.19/ final/）
├── dist-v21/                   ★ v4.19 参考产物（57 文件）
├── imported/                   v4.17–v4.19 三个 book 项目溯源归档
└── _legacy/                    冻结归档（只读，勿执行）
    ├── old-chain-v416/         旧链：capabilities 28 卡+meta+bundle / candidates / scripts / eval-archive
    └── dist-legacy/            旧产物 dist-v12 … dist-v19（git 留痕；v3–v11 在本地 _legacy-local/，不入库）
```

已装技能（`~/.workbuddy/skills/fda-pchf-food-safety`）是**用户级**、随用户跨项目；本仓库是**开发源**。
两者当前内容一致（v4.19）。已装目录自带孤立 `.git`（1 提交、无远端），**勿在其中执行 git 操作**。
