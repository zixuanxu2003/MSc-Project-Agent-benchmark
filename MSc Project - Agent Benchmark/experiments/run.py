def main():
    # 1. 加载任务
    task = load_task("pandas_l3")
    
    # 2. 根据任务选择tools（自动）
    tools = setup_tools_for_task(task)
    # → 如果是pandas任务，自动加载python_tool
    # → 如果需要搜索，自动加载search_tool
    
    # 3. 初始化Agent
    agent = OpenAIAgent(api_key=...)
    
    # 4. 执行（自动）
    executor = AgentExecutor(agent, tools)
    state = executor.execute(task)  # 这里自动跑
    
    # 5. 验证（自动）
    verifier = get_verifier(task["task_id"])
    result = verifier.verify(state)
    
    # 6. 保存结果
    save_result(task, state, result)