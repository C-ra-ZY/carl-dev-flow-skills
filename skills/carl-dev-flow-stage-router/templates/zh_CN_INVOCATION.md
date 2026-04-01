# Hephaestus + Oracle + Sisyphus Workflow 中文快速调用模板

这份模板用于快速触发整套 workflow family，减少每次都要重新组织提示词的负担。

## 1. 从零开始一个新需求

```text
请启动 carl-dev-flow-orchestrator。
当前还没有 requirements 或 technical spec，请从 requirements-development 开始。
目标：<一句话描述需求>
约束：<时间/技术/产品约束>
输出：先给出 requirements draft，然后进入 Hephaestus 主导、Oracle 审查的收敛流程。
```

## 2. 继续当前流程，但不确定卡在哪个阶段

```text
请用 carl-dev-flow-stage-router 判断我们当前处于哪个阶段，
明确：current stage、lead role、current artifact、next artifact、immediate next action，
然后直接推进下一步，不要只停留在总结。
```

## 3. 进入需求澄清阶段

```text
请加载 carl-dev-flow-requirements。
我要先把需求文档打磨清楚，再进入技术方案。
请由 Hephaestus 主导问答澄清，产出 requirements draft，并安排 Oracle 做独立 review。
```

## 4. 进入技术方案确认阶段

```text
请加载 carl-dev-flow-tech-spec。
需求已经基本稳定，现在需要形成 technical spec draft。
请由 Hephaestus 主导 technical spec draft，覆盖架构、接口、失败处理、可运维性、性能假设，并组织 Oracle review；如实现复杂度会反向约束方案，可引入 Sisyphus 做可实现性反馈。
```

## 5. 进入开发执行阶段

```text
请加载 carl-dev-flow-implementation。
requirements final 和 technical spec final 已经就绪。
请由 Hephaestus 把实现拆成细粒度任务，明确依赖顺序、验收标准和验证方式，并把高难度编码与修复执行优先交给 Sisyphus。
```

## 6. 进入递归评审和修复阶段

```text
请加载 carl-dev-flow-review-loop。
当前代码已经有实现，请组织 Oracle + 用户先产出 review memo draft，
再由 Hephaestus 综合 findings、拆解修复，并交给 Sisyphus 执行，随后进入下一轮复审。
Oracle 是主要审查者；如需额外专家意见，只能作为顾问性输入，不能替代 Oracle 自己完成 review。
```

## 7. 明确仲裁规则

```text
如果 Hephaestus 和 Oracle 对方案或修复方向有分歧，请把分歧明确写出来，
然后由我做最终裁决，并把我的决定写回 artifact 或 review memo。
```

## 8. 强调干净交付

```text
请按 workflow 推进，但不要停在分析。
我要的是可以交付的结果：文档要落地、代码要验证、review 要闭环。
```

## 使用建议

- 不确定阶段时，优先用 `carl-dev-flow-stage-router`
- 跨阶段总控时，优先用 `carl-dev-flow-orchestrator`
- 已经明确当前工作性质时，直接点名对应子 skill，效率更高
- 有分歧时，直接复用上面的仲裁模板，避免 agent 自行兜底
