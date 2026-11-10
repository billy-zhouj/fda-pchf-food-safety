# `_legacy/` — 冻结归档（只读）

2026-11-10 v4.19 双血缘收口时冻结。**这里的东西不再参与构建，不要执行其中任何脚本。**

## 结构

| 路径 | 内容 | 说明 |
|---|---|---|
| `old-chain-v416/capabilities/` | 28 张 RIA++ 卡 + `_meta-*.yaml` + bundle 三件套（verified.yaml / destinations.json / book/） | 旧链（v4.16 冻结态）。这 28 张卡与 dist-v21 中同名卡**逐字节一致**，属冗余快照 |
| `old-chain-v416/candidates/` | 旧链阶段 1 候选（glossary / cases / counter-examples） | 旧链 `assemble_bundle.py` 的输入 |
| `old-chain-v416/scripts/` | `assemble_bundle.py`、`install_v3.py`–`install_v17.py`、apply/append/convert/verify/score 等一次性脚本 | 全部带 DEPRECATED 守卫（`exit 2`）。仅路线 A 研究可 `ALLOW_DEPRECATED_CANGJIE=1` 放行 |
| `old-chain-v416/eval-archive/` | v4.7–v4.11 评测包与报告、convert-report、manifest.yaml | 历史审计轨迹 |
| `dist-legacy/dist-v12`–`dist-v19` | 旧链历史产物 | v3–v11 与 `dist-update` 在本地 `_legacy-local/dist-untracked/`，**不入库** |

## 为什么保留

1. **审计可追溯**：每一条旧结论都能回查当时的构建输入。
2. **路线 A 备用**：若未来要把 23 张新卡按旧链的 RIA++ + assemble_bundle 体系重编，需要这些输入。
   但在完成前，`assemble_bundle.py` 会用 v4.16 的 28 卡覆盖 bundle，**生产环境禁止运行**。

## 现役构建链

见 `.cangjie/README.md`：`build_v4.19.py`（唯一全量构建）+ `install_v18.py`（唯一安装）。
