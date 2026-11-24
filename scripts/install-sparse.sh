#!/usr/bin/env bash
# 用法：
#   bash scripts/install-sparse.sh           应用/刷新 sparse 模式：工作树只留交付物
#   bash scripts/install-sparse.sh --check   自检（不改动）：SKILL.md 必须恰好 1 个
#   bash scripts/install-sparse.sh --full    关闭 sparse，还原完整工作树（构建链需要）
#
# 背景：技能加载器会递归扫描本目录、把每个 SKILL.md 都注册成一条技能。完整检出时
# 有 12 个 SKILL.md（根 1 + _legacy 8 + build 2 + dist-v21 1），会出现重复/歧义条目。
# 详见仓库根目录 README.md 第 3.1 节。

set -euo pipefail

# Git Bash 会把 '/SKILL.md' 当路径翻译成 'E:/Program Files/.../SKILL.md'，必须关掉。
export MSYS_NO_PATHCONV=1

# sparse 保留清单：交付物 + 文档 + 本脚本（否则脚本自己会被遮掉）
PATTERNS=(
  '/SKILL.md'
  '/README.md'
  '/test-prompts.json'
  '/.gitignore'
  '/references/'
  '/scripts/'
)

die() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }

cd "$(git rev-parse --show-toplevel 2>/dev/null)" || die "当前目录不在 git 仓库内"
[ -f SKILL.md ] || die "根目录没有 SKILL.md，这不像技能包仓库"

count_skill_md() {
  find . -name SKILL.md -not -path './.git/*' | wc -l | tr -d ' '
}

sparse_on() {
  [ "$(git config --get core.sparseCheckout 2>/dev/null || echo false)" = "true" ]
}

case "${1:-}" in
  ''|--apply)
    sparse_on || git sparse-checkout init --no-cone
    git sparse-checkout set "${PATTERNS[@]}"
    ;;
  --check)
    ;;
  --full)
    if sparse_on; then
      git sparse-checkout disable
      printf '已关闭 sparse，工作树恢复完整（%s 个文件）。构建完记得重新运行本脚本。\n' \
        "$(git ls-files | wc -l | tr -d ' ')"
    else
      printf '当前已是完整工作树，无需关闭。\n'
    fi
    ;;
  -h|--help)
    sed -n '2,10p' "$0" | sed 's/^# \{0,1\}//'
    exit 0
    ;;
  *)
    die "未知参数：$1（用 --help 看用法）"
    ;;
esac

n=$(count_skill_md)
printf 'SKILL.md 数量：%s（期望 1）\n' "$n"
if [ "$n" -ne 1 ]; then
  printf 'WARN: 多于 1 个会在技能列表里出现重复条目，清单如下：\n' >&2
  find . -name SKILL.md -not -path './.git/*' | sed 's/^/  /' >&2
  if [ "${1:-}" = "--check" ]; then
    exit 1
  fi
  printf 'WARN: 运行 `bash scripts/install-sparse.sh` 可收敛到 1 个。\n' >&2
fi

if [ "${1:-}" = "--check" ]; then
  printf 'OK：工作树与索引正常。\n'
fi
