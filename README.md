# fda-pchf-food-safety（技能包 × 权威仓库）

FDA 人类食品危害分析与基于风险的预防控制（PCHF / 21 CFR Part 117 / FSMA）技能包。
本仓库同时承载**两种形态**，改任何内容前先读第 2、3 节。

- 远端：`https://github.com/billy-zhouj/fda-pchf-food-safety.git`（私有）
- 本地分支 `master` 跟踪 `origin/main`

---

## 1. 当前状态

| 项 | 值 |
|---|---|
| 版本 | **v4.22** |
| 能力卡 | **35 张主卡** + 20 张子卡（imports 10 / labeling 5 / additives 5） |
| 术语 | **356 条**（YAML 块 t01–t356） |
| 测试用例 | **239 条**（`test-prompts.json`，version 4.22） |
| 来源类数 | **27 类**（法规正文 12 套 + FDA 指南 6 类 + 检查程序与内部作业 9 类） |
| 法规编号 | **12 套**独立编号，见 `SKILL.md` 原则 37 |

`SKILL.md` 的 `metadata.cangjie.capability-count` 必须与主卡数一致，提交前核对。

---

## 2. 两种形态与目录职责

```
<repo root>
├── SKILL.md                ┐
├── references/             ├─ ① 交付物：可直接安装的技能包（62 个文件）
├── test-prompts.json       ┘
│
├── source-*.md             ┐
├── books/  imported/       ├─ ② 权威仓库：来源正文、构建链、历史产物
├── build/                  │   （v4.19 双血缘决议，见 .cangjie/README.md）
├── dist-v21/               │
├── _legacy/                │
└── .cangjie/               ┘
```

- **根目录交付物**是唯一被技能加载器读取的部分；`dist-v21/`、`build/`、`_legacy/` 是构建与溯源资产，**不进安装态**。
- 两者同属一个仓库、同一份历史（v4.22 时以 `--allow-unrelated-histories` 合并过一条旧 `main`）。

---

## 3. 已知坑（三个，都踩过）

### 3.1 嵌套 `SKILL.md` 会变成「重复技能」

**加载器的行为（实测确认，非推测）**：

- 递归扫描 `~/.workbuddy/skills/<包名>/` 下**最深 5 层**，**每一个 `SKILL.md` 都注册成一条技能**；
- 没有 `.skillignore` 之类的忽略机制；跳过名单硬编码为 `.DS_Store` / `Thumbs.db` / `desktop.ini` / `.git` / `node_modules` / `__MACOSX` / `__pycache__`；
- 唯一的「关」是 `~/.workbuddy/settings.json` 的 `skillOverrides`，键取 frontmatter `name`，值 `off` / `user-invocable-only` / `name-only`，语义是**禁止模型自动调用**，不是「不被扫描」；**同名技能一关全关**，无法只关副本。

本仓库完整检出时会有 **12 个** `SKILL.md`（根 1 + `_legacy/dist-legacy/dist-v12…v19` 8 + `build/v4.16-baseline`、`build/v4.19/final`、`dist-v21` 各 1），因此**在安装目录里必须用 sparse-checkout 只保留交付物**：

```bash
cd ~/.workbuddy/skills/fda-pchf-food-safety
MSYS_NO_PATHCONV=1 git sparse-checkout init --no-cone
MSYS_NO_PATHCONV=1 git sparse-checkout set \
  '/SKILL.md' '/README.md' '/test-prompts.json' '/.gitignore' '/references/'
```

自检（**必须等于 1**）：

```bash
find ~/.workbuddy/skills/fda-pchf-food-safety -name SKILL.md | wc -l
```

> Git Bash 会把 `/SKILL.md` 当路径翻译成 `E:/Program Files/.../SKILL.md`，必须加 `MSYS_NO_PATHCONV=1`；
> 不加前导 `/` 时模式会匹配任意深度的同名文件，等于没修。索引与远端不受影响，`git ls-files` 仍是全量。

### 3.2 本机 git 走 MITM 代理，直连会报证书错

本机 `https_proxy=127.0.0.1:57168`，schannel 报 `CRYPT_E_NO_REVOCATION_CHECK`，openssl 报 `unable to get local issuer certificate`。可用写法（逐条命令生效，不写进配置）：

```bash
git -c http.sslBackend=openssl fetch origin                # 读
git -c http.sslVerify=false      push  origin HEAD:main    # 写
```

读 `origin/main:<path>` 形式的对象时也要加 `MSYS_NO_PATHCONV=1`。

### 3.3 构建链不能在 sparse 状态下跑

`build_v4.19.py` 的验收条件是「产物与 `dist-v21` **57 个文件逐一 sha256 相等**」，它需要 `build/` 下的基线目录。sparse 状态下这些目录不在工作树里：

- 要么 `git sparse-checkout disable`（嵌套 `SKILL.md` 会回来、重复技能随之上线），
- 要么**另 clone 一份**专门跑构建（推荐）。

---

## 4. 日常改动流

1. 在安装目录改 `SKILL.md` / `references/` / `test-prompts.json`（这是交付物本体）。
2. 校验：引文逐字核对、卡数 / 类数 / 套数三套计数一致、`test-prompts.json` 可解析。
3. `git add -A && git commit`（中文提交信息，写清法源条号与校验结果）。
4. `git -c http.sslVerify=false push origin HEAD:main`，确认 `git status -sb` 干净、`ls-remote` 与本地 HEAD 一致。
5. **不加 `--force`、不改已推送提交**，除非明确要求。

---

## 5. 引用纪律（回答问题时）

- 效力三层：法规正文（`shall` / `must`）＞ FDA 指南（`should`）＞ CPGM / CP / IOM（检查员视角，**不创设企业义务**）。
- 法规引用写〔§ 117.xxx〕[pdf-page N] 这类带编号的形式；12 套编号互不替代。
- **21 CFR Part 1 的 Subpart L / S / O 三套编号（〔§ 1.5xx〕〔§ 1.13xx/1.14xx〕〔§ 1.9xx〕）必须带 subpart 归属**，不得只说「part 1」。
- 未收正文一律标「转引未收」，不得凭记忆补数值。

---

## 6. 相关文档

- 能力路由与红线：`SKILL.md`
- 能力索引：`references/capability-index.md`
- 术语：`references/glossary.md`；速查：`references/cheatsheet.md`；规模与沿革：`references/overview.md`
- 构建链决议：`.cangjie/README.md`、`_legacy/README.md`
