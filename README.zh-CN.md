# Agent Project OS

一套面向 Codex 与 Claude Code 的按需工具：需要时搭建或检修长期 Memory 与 Markdown 项目结构；结构可用后，插件退出日常工作。

[English](README.md)

## 什么时候用

- 想让 Agent 记住稳定偏好，或记住各项目放在哪里；
- 要启动新项目、接手混乱项目，或整理散落文件；
- 项目用久后，新会话已经很难看懂或续接；
- 想同时比较多个 Markdown 项目；
- 项目没有自己的更新流程，而你明确想让 Agent 做一次通用状态盘点并先给修改提案；
- 确实不知道该选哪项 Project OS 能力。

不要仅仅因为要继续一个已知项目、写文章、分析资料或处理普通项目工作而调用它。此时 Agent 应通过 Memory 找到项目稳定入口和当前状态文件，然后直接工作。

## 第一次使用

安装一个语言包后，直接用自然语言说明要搭建或检修什么：

```text
帮我建立一套长期记忆，记住我的工作偏好和项目位置。
帮我启动一个研究项目，做成新 Agent 会话也能续接的结构。
这些文件很散，帮我整理成一个能长期维护的项目。
检查一下这个项目的结构，先不要修改。
比较这 4 个项目，看看哪个已经受阻。
```

只读流程可以在已给定或已授权的范围内检查文件；任何写入前，Agent 都会展示精确目标与拟写内容。项目文件与 Workspace Memory 分别确认；新项目的 Memory 路由在你批准那一项精确修改前，只是候选方案。

## 语言包

| 工作语言 | 只安装这一包 |
| --- | --- |
| 中文 | `agent-project-os` |
| English | `agent-project-os-en` |

不要同时安装两包；它们有意提供相同的 Skill 名。

当前分支是 V1.0.0 发布候选。仓库已同时提供两种宿主的 Marketplace 清单，但最终公开 GitHub 安装命令要等第 4 阶段用真实仓库 URL 在全新 Codex 和 Claude Code 环境中验证后才发布。在此之前，请通过宿主的本地 Marketplace／插件源流程添加本仓库，并且只选择一个语言包。

包内详情：

- [中文包](plugins/agent-project-os/README.md)
- [英文包](plugins/agent-project-os-en/README.md)
- [双语分发契约](distribution/BILINGUAL-DISTRIBUTION.zh-CN.md)

## 搭建完成后如何工作

真正留下来的不是一个永远在线的路由器，而是一组宿主 Agent 不依赖本插件也能读取的普通文件：

```text
Workspace Memory → 项目稳定入口 → 当前状态事实源 → Agent 日常工作
```

只有当这套结构需要创建、检查或修复时，再调用 Agent Project OS。

Apache-2.0，许可证见各语言包。
