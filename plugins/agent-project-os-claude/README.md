# Agent Project OS · Claude Code 中文包

这是 Agent Project OS 的 Claude Code 专用发布包。它帮助文件系统型 Agent 按“单一物理 Memory 库、薄总索引、按需主题文件、项目稳定入口”的方法建立长期工作系统。结构建立后，插件应当隐身；日常工作由 Claude Code 直接读取 Memory 和项目文件完成。

## 适合这些时刻

- 第一次建立长期 Memory，整理稳定偏好、边界与项目位置；
- 想让 Codex 与 Claude Code 共用同一物理 Memory，不再维护两份副本；
- 启动新项目、接手别人的项目，或把散落笔记整理成项目；
- 现有项目的入口、状态文件或事实来源已经混乱；
- 明确要求只读审查一个项目的结构；
- 明确要求比较多个项目；
- 用户手动调用 `/agent-project-os:state-handoff`，要求在没有项目本地更新流程时生成一次状态交接提案；
- 确实不知道上述哪种能力适合当前问题。

## 不适合这些时刻

- 已知项目的普通续接、写作、研究、执行或交付；
- 仅仅询问“这个项目下一步做什么”；
- 已经有明确项目路径和任务，只需要宿主 Agent 开始工作；
- 把每天的聊天、进度或临时阻塞自动抄进 Memory。

日常续接应走：

```text
Workspace Memory 或精确项目路径 → 薄宿主适配入口 → 项目稳定入口 → 当前状态事实源 → 宿主 Agent 直接工作
```

这条链路一旦可用，就不需要再次调用 Agent Project OS。

## Claude Code 显式调用边界

- `/agent-project-os:project-os` 是低频能力选择帮助，已使用 `disable-model-invocation: true` 禁止模型自动调用。
- `/agent-project-os:state-handoff` 是通用状态交接，同样只允许用户手动调用。
- 其他 4 个 Skill 仍按明确的搭建或检修请求自然匹配；日常续接不调用本插件。

## 第一次使用

安装完成后新开一个任务，只需输入这一条首启提示：

```text
我第一次使用 Agent Project OS。请从零带我建立长期 Memory，并从我的真实工作中选出 1 个适合长期跟进的项目。一次只问我一个容易回答的问题，写入前先让我确认。
```

AI 会用白话、一次一问地带你从 2–3 件真实工作中选出 1 个项目。项目文件与 Memory 会分开展示、分开确认，只配置你选择的宿主；最后在禁用插件的新会话中验证项目仍可续接。毕业后平时只说“继续<项目名>”，不需要再调用 Project OS。

## 安全边界

- 会写文件的流程，先展示精确目标路径与拟写内容，再等待确认。
- 项目文件写入和 Workspace Memory 写入分别确认，不能用一次批准代替两次。
- `launch-project` 只生成 Memory 路由候选；只有 `bootstrap-workspace` 检查冲突并获得单独确认后，才能登记到 Memory。
- 结构审查默认且始终只读；批准修复后，由 `launch-project` 在另一个明确流程中执行。
- 项目进展、临时阻塞、客户细节与敏感事实留在项目内，不提升为长期 Memory。
- 没有项目路径时，不假装已核对项目，也不替项目生成普通日常行动。
- 若要求严格的路径续接，`launch-project` 会单独提议 Codex `AGENTS.md` 或 Claude Code `CLAUDE.md`；它们只路由到同一稳定入口，不复制项目状态，仍需用户确认后写入。
- 全新用户的标准 Memory preset 默认只有一个物理库；Codex 与 Claude Code 入口指向该库，不创建镜像、副本或双写后端。
- Memory 内容、物理目录、用户所选宿主入口、全局规则、已实证需要的宿主读写权限和本地 Git 操作分开列出；未明确批准的范围不执行。

## 安装

本包名称是 `agent-project-os`，适用于中文工作界面。本分支是面向新用户封闭测试的中文专用分支，插件市场只显示这一包。

当前版本是 `1.1.0-beta.1`。Codex 与 Claude Code 已拆成两个宿主专用包；本包只包含 Claude Code 清单和 Claude Code 支持的显式调用 frontmatter。上一轮 B-03 First Run 严格门为 0/3，整改尚待重新实测；本包仅供封闭测试，不宣称为稳定版。

Skills 是 `skills/` 下的 Markdown 指令，不包含后台服务或自动网络请求。宿主 Agent 仍会按照你批准的范围读取或修改工作区文件。

## Skill 参考

| Skill | 只在何时使用 |
| --- | --- |
| `bootstrap-workspace` | 建立或整理长期 Memory；确认项目路由 |
| `launch-project` | 启动、接手或整理一个项目；执行已批准的精确结构修复 |
| `review-project-structure` | 明确要求只读审查单个项目结构 |
| `review-portfolio` | 明确要求比较多个项目 |
| `state-handoff` | 仅在项目没有本地更新流程且用户手动调用 `/agent-project-os:state-handoff` 时使用 |
| `project-os` | 手动调用 `/agent-project-os:project-os`，并明确表示不知道该选哪项 Project OS 能力 |

## 状态

A 轨误触发回归已通过；B-03 First Run 严格门与双轨合流仍未关闭。旧 V1.0.2 证据只保留为历史基线，不覆盖 `1.1.0-beta.1`。本候选供新用户封闭测试，不打稳定 tag，也不宣称全部发布门禁已通过。

Apache-2.0。见 [LICENSE](LICENSE)。
