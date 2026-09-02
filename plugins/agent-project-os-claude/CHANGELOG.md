# 更新日志

此处记录 Agent Project OS 的所有重要变更。

## Unreleased

## 1.1.0-beta.1 — 2026-09-02

- 将 `project-check-in` 改名为 `state-handoff`，降低“今天做什么 / 继续项目”等日常续接请求的误触发风险。
- 新增 Greenfield First Run：用白话一次一问，从 2–3 件真实工作中确认 1 个项目，项目与 Memory 分开批准并做独立续接验收。
- 拆分 Codex 与 Claude Code 宿主专用包：共享工作流正文，分别使用 Codex `openai.yaml` 和 Claude Code `disable-model-invocation` 表达显式调用边界。
- 收紧 First Run 的宿主、读写边界、项目批准、Memory 六桶批准和禁用插件毕业测试合同。
- 本版本为中文封闭测试候选；B-03 严格行为门仍在复验，不作为稳定发布。

## 1.0.2 — 2026-08-16

- 对全新用户新增标准共享 Memory preset：单一物理库、薄 `MEMORY.md`、按需主题文件和 Codex / Claude Code 双宿主入口。
- 增加本地 Git 恢复边界、宿主规则最小合并，以及按宿主与读写操作区分的实证后权限提案。
- 保留精确单文件目标的高优先级；用户未要求多文件时不自动扩展 preset。
- 禁止镜像、复制或双写同步，禁止强制覆盖既有链接或全局规则。

## 1.0.1 — 2026-08-16

- 将产品定位收窄为按需搭建与检修工具；普通项目工作不再经过插件。
- 新项目写入项目文件后，只生成待确认的 Memory 路由候选；Memory 另行确认。
- 重写首次使用与 Skill 参考，用户无需先学习 `project-os`。
- 补齐 Codex 与 Claude Code 的双语仓库 Marketplace 清单。
- 修复显式 Memory 目标边界：不再套用宿主内部记忆布局，也不在未授权时枚举或探测目标目录。
- 为严格路径续接增加薄宿主适配入口合同：Codex `AGENTS.md`、Claude Code `CLAUDE.md` 只路由到同一稳定入口，不复制项目状态。

## 1.0.0 — 2026-07-31

首个审核候选版本。

- 发布 6 个 Skill：低频项目路由、工作区初始化、项目启动、显式项目 check-in、结构审阅和项目组合审阅。
- 通过 L0--L4 发布证据，验证「先确认、后写入」、默认只读审阅、精简项目组合和敏感上下文边界。
- 提供 Codex 与 Claude Code 插件清单、Apache-2.0 许可证、中英文仓库说明及双语分发契约。
- 已针对已安装的本地插件显式验证 Codex `$project-os` 调用，全程未写入项目文件。

## 0.2.0 — 2026-07-31

- 新增 `project-os` 与 `project-check-in`，完成 v0.2 行为验证周期。
