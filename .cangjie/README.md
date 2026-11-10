# `.cangjie/` 构建脚本索引（2026-11-10，v4.19 收口后）

> ⚠ **先读这里再跑任何脚本。** 本目录同时存在**新旧两套构建链**，旧链脚本已被加
> `DEPRECATED` 守卫：默认 `exit 2` 拒绝执行，仅当显式
> `export ALLOW_DEPRECATED_CANGJIE=1` 才放行（放行仅用于「路线 A 全量移植」）。

## 1. 两套构建血缘（为什么会有两套）

| | 旧链（v4.16 及以前） | 新链（v4.17–v4.19，现权威） |
|---|---|---|
| 卡源 | `cards/*.md`（28 张 RIA++ 六段卡）+ `_meta-*.yaml` | 各 book 项目的 `candidates/` + `verified.md` |
| 组装 | `assemble_bundle.py`（SLUGS 硬编码 28 卡）→ `verified.yaml`/`destinations.json`/`book/` | 各 book 的 `apply_v4.1x.py` / `convert_*.py` 叠加安装 |
| 产物 | `dist-v3` … `dist-v20` | 直接叠加进已装技能，收口后定格为 **`dist-v21`（v4.19 成品镜像）** |
| 状态 | **已弃用，禁止日常执行**（守卫拦截） | 权威；v4.19 收口（路线 B）后以成品定权威，旧链保留待路线 A 移植 |

v4.17–v4.19 由 3 个独立 book 项目（`iom-2026-ch6` / `cfr-part101-2026` /
`cfr-part172-2026`）各自叠加安装，**未经旧链编译**，因此旧链 `SLUGS` 仍是 28 卡。
误跑旧链会用 v4.16 数据覆盖 `.cangjie/capabilities/` 下的 bundle 文件，
误跑旧安装器会把已装技能退回旧版。这就是守卫存在的原因。

## 2. 脚本分类

### ✅ 可用（当前权威链）
| 脚本 | 作用 | 指标 |
|---|---|---|
| `install_v18.py` | 把 **`dist-v21`（v4.19）** 安装到用户级 `~/.workbuddy/skills/fda-pchf-food-safety`（备份→整目录镜像→官方校验→sha256 比对） | 51 卡（递归）/ 318 术语 / 204 用例 / version 4.19 |

### 🚫 已弃用（守卫拦截，`ALLOW_DEPRECATED_CANGJIE=1` 可强跑，仅限路线 A）
- **旧链编译/组装**：`assemble_bundle.py`（28 卡 → bundle 三件套）。
- **旧版安装器** `install_v3.py` … `install_v17.py`（共 15 个，按下表会把已装技能退回对应旧版）：

| 脚本 | SRC | 退回到的版本 |
|---|---|---|
| `install_v3.py` | `dist-v3` | v3 |
| `install_v4.py` | `dist-v4` | v4 |
| `install_v5.py` | `dist-v5` | v4.1 |
| `install_v6.py` | `dist-v9` | v4.5（注意：脚本号与 dist 号历史漂移） |
| `install_v7.py` | `dist-v10` | v4.5 后期 |
| `install_v8.py` | `dist-v11` | v4.6 |
| `install_v9.py` | `dist-v12` | v4.7 |
| `install_v10.py` | `dist-v13` | v4.8 |
| `install_v11.py` | `dist-v15` | v4.11 |
| `install_v12.py` | `dist-v16` | v4.12 |
| `install_v13.py` | `dist-v17` | v4.13 |
| `install_v14.py` | `dist-v18` | v4.14 |
| `install_v15.py` | `dist-v19` | v4.15 |
| `install_v16.py` | `dist-v19` | v4.15.1（27 卡 / 223 术语 / 158 用例） |
| `install_v17.py` | `dist-v20` | **v4.16**（28 卡 / 233 术语 / 168 用例）← 最常被误跑的一个 |

### 📦 历史一次性脚本（无守卫、无需跑；当时任务已固化进产物/文档，重跑无意义且可能破坏现状）
- 各版本增量回补：`apply_v4_*.py`、`apply_legacy_eval_state.py`、`append_v4*.py`、
  `append_lmono_*.py`
- 来源转换：`convert_*.py`、`finalize_*.py`、`fix_*.py`
- 引文核验：`verify_*_quotes.py`
- 评测：`build_*_eval_suites.py`、`check_*_routing.py`、`score_*.py`
  （⚠ v4.12 起评测欠账：若重跑，**必须**基于 `dist-v21` 重写断言，旧脚本的卡数/来源数断言全部过期）
- 数据文件：`part108_header.md`、`part120_header.md`、`cp847_header.md`、`v4-*-eval-report.md`

## 3. 规则（硬性）

1. **安装只走 `install_v18.py`**（当前指向 dist-v21）。出新版本时新建 `install_v19.py`
   并给旧 `install_v18.py` 加守卫，不改旧脚本的 SRC。
2. **禁止**在路线 A 完成前执行 `assemble_bundle.py`（含强跑）——产物与 v4.19 现状冲突。
3. 任何脚本改动后：`python -c "import ast; ast.parse(open(...))"` 语法自检 →
   真实运行前先在临时 DST 验证 → 再跑正式目标。
4. 守卫环境变量 `ALLOW_DEPRECATED_CANGJIE` 是**一次性**放行：用后即忘，
   不要写进 shell profile 或自动化任务。

## 4. 目录地图（构建产物）

```
仓库根/
├── dist-v3 … dist-v20/   旧链历史产物（v3–v4.16），仅存档
├── dist-v21/             ★ 当前权威产物（v4.19 成品镜像，57 文件，与已装技能 hash 一致）
├── dist-update/          旧链增量更新残留
├── imported/             v4.17–v4.19 三个 book 项目的溯源归档（source + candidates + apply 脚本）
├── source-*.md           第一~第二十来源的 eCFR/PDF 转换原文（旧链书源；Part 101/172 原文见 imported/）
└── .cangjie/             本目录（脚本 + 历史评测报告）
    └── capabilities/     旧链 28 卡 cards/ + _meta-*.yaml + bundle 三件套（v4.16 冻结态）
```

已装技能（`~/.workbuddy/skills/fda-pchf-food-safety`）是**用户级**、随用户跨项目；
本仓库是**开发源**，两者当前内容一致（v4.19），但已装目录自带孤立 `.git`（1 提交、无远端），
勿在其中执行 git 操作（避免再次分叉——v4.17–19 分裂的根源）。
