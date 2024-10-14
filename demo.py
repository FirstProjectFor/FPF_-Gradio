import gradio as gr


# 为模型定义一个简单的函数
def add_numbers(a, b, op, code, date,checkbox,slider):

    print(code)
    print(date)
    print(checkbox)
    print(slider)


    operation = op

    if operation == "+" :
        return a+b
    elif operation == "-" :
        return a-b
    elif operation == "*" :
        return a*b
    elif operation == "/" :
        return a/b
    elif operation == "%" :
        return a%b
    
    return "未知运算符"


# 使用更新的语法创建一个Gradio界面
interface = gr.Interface(
    fn=add_numbers,
    inputs=[
        gr.Number(label="A"), 
        gr.Number(label="B"), 
        gr.Radio(choices=["+", "-", "*", "/", "%"], value="+", label="运算"),
        gr.Code(label="code", value="print('hello world')"),
        gr.DateTime(label="date"),
        gr.CheckboxGroup(choices=["a", "b", "c"], label="checkbox"),
        gr.Slider(minimum=0, maximum=100, value=50, label="Slider")
        ],
    outputs=[gr.Number(label="结果")],
    title="简单计算模型",
    description="输入两个数字进行简单计算",
    clear_btn=None
)

# 启动界面
interface.launch()