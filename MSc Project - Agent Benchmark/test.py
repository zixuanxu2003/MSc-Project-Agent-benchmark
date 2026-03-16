from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END


# --- 1. 定义状态 ---
class AgentState(TypedDict):
    task: str
    code: Optional[str]
    feedback: Optional[str]
    iterations: int
    success: bool


# --- 2. 定义节点逻辑 ---

def researcher(state: AgentState):
    """模拟 Research 阶段，确定算法逻辑"""
    print(f"\n[Round {state['iterations'] + 1}] Researcher: 分析任务...")
    # 模拟研究结论：第一次可能不全面，第二次更深入
    logic = "需要实现一个加法函数" if state['iterations'] == 0 else "需要实现加法并确保返回整数"
    return {"iterations": state["iterations"] + 1}


def coder(state: AgentState):
    """模拟 Coding 阶段，编写代码"""
    print(f"[Round {state['iterations']}] Coder: 正在编写/修改代码...")
    # 第一次故意写错（比如变量名写错），第二次写对
    if state['iterations'] == 1:
        code = "def add(a, b): return a + c  # 故意制造 NameError"
    else:
        code = "def add(a, b): return a + b"
    return {"code": code}


def executor(state: AgentState):
    """真实执行代码并捕获报错 --- 这是 Jeff 最看重的反馈闭环"""
    print(f"[Round {state['iterations']}] Executor: 正在验证代码...")
    local_vars = {}
    try:
        # 实际执行代码
        exec(state['code'], {}, local_vars)
        # 测试用例验证
        if local_vars['add'](1, 2) == 3:
            print(">>> 验证通过！")
            return {"feedback": "Success", "success": True}
        else:
            return {"feedback": "Logic Error: Result not match", "success": False}
    except Exception as e:
        error_msg = f"Runtime Error: {str(e)}"
        print(f">>> 验证失败: {error_msg}")
        return {"feedback": error_msg, "success": False}


# --- 3. 构建图逻辑 ---

workflow = StateGraph(AgentState)

# 添加节点
workflow.add_node("researcher", researcher)
workflow.add_node("coder", coder)
workflow.add_node("executor", executor)

# 连线
workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "coder")
workflow.add_edge("coder", "executor")

# 条件边：判断是否需要重试（Self-evolving）
workflow.add_conditional_edges(
    "executor",
    lambda x: "end" if x["success"] else "retry",
    {
        "retry": "researcher",  # 报错了回到研究节点
        "end": END
    }
)

# 编译
app = workflow.compile()

# --- 4. 运行 Demo ---
if __name__ == "__main__":
    initial_state = {
        "task": "写一个加法函数并验证",
        "code": None,
        "feedback": None,
        "iterations": 0,
        "success": False
    }

    # 启动图运行
    app.invoke(initial_state)