# executor.py - 这是通用的执行逻辑
class AgentExecutor:
    def execute(self, task):
        # 不管什么任务，流程都一样
        while not done:
            # 1. Agent 想一步
            action = agent.step(state)
            
            # 2. 执行工具
            if action.type == "call_tool":
                result = tools[action.tool_name].execute(...)
            
            # 3. 检查是否结束
            if action.type == "answer":
                done = True
        
        return state  # 返回执行记录