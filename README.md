# Agent Project OS 中文实操版

这是给培训实操使用的中文分支，只保留中文插件包 `agent-project-os`。

## 安装方法

在 Codex 里添加插件市场时填写：

```text
来源：terrence741-cell/agent-project-os
Git 引用：feat/v1-first-run-zh-only
稀疏路径：留空；如果系统不允许留空，就填 .
```

添加市场后，在插件列表里安装：

```text
agent-project-os
```

这个中文分支不会显示英文包，避免误装。

## 下午实操

安装完成后，新开一个对话，对 AI 说：

```text
使用 Agent Project OS，帮我建立长期 Memory 系统，并创建 1-2 个以后新会话也能继续接手的项目文件夹。
```

写入文件前，AI 会先列出要写到哪里、写什么内容。看清楚后再确认写入。

## 适合做什么

- 建立长期 Memory，记录稳定偏好、规则和项目位置；
- 创建项目文件夹、项目入口和当前状态文件；
- 让新会话以后能通过 Memory 找到项目并继续工作；
- 检查一个 Markdown 项目的结构是否容易续接。

不要把它当成日常项目助手。项目结构搭好后，平时继续项目应由 AI 直接读取 Memory 和项目状态文件。
