import asyncio
import tkinter as tk
from tkinter import messagebox
from telegram import Bot

# Função para promover um membro a administrador com permissões selecionadas
async def promover_para_admin(token, group_id, user_id, permissions):
    try:
        bot = Bot(token=token)
        
        # Promover o membro a administrador com as permissões especificadas
        await bot.promote_chat_member(
            chat_id=group_id,
            user_id=user_id,
            can_change_info=permissions["can_change_info"].get(),
            can_post_messages=permissions["can_post_messages"].get(),
            can_edit_messages=permissions["can_edit_messages"].get(),
            can_delete_messages=permissions["can_delete_messages"].get(),
            can_invite_users=permissions["can_invite_users"].get(),
            can_restrict_members=permissions["can_restrict_members"].get(),
            can_pin_messages=permissions["can_pin_messages"].get(),
            can_promote_members=permissions["can_promote_members"].get()
        )
        
        messagebox.showinfo("Sucesso", "Usuário promovido a administrador com sucesso!")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para iniciar a execução da função assíncrona
def promover_admin():
    token = token_entry.get()
    group_id = group_id_entry.get()
    user_id = user_id_entry.get()
    
    if token and group_id and user_id:
        try:
            group_id = int(group_id)  # Converter o ID do grupo para inteiro
            user_id = int(user_id)    # Converter o ID do usuário para inteiro
            
            # Criar um dicionário de permissões com as seleções das caixas de seleção
            permissions = {
                "can_change_info": can_change_info_var,
                "can_post_messages": can_post_messages_var,
                "can_edit_messages": can_edit_messages_var,
                "can_delete_messages": can_delete_messages_var,
                "can_invite_users": can_invite_users_var,
                "can_restrict_members": can_restrict_members_var,
                "can_pin_messages": can_pin_messages_var,
                "can_promote_members": can_promote_members_var
            }
            
            asyncio.run(promover_para_admin(token, group_id, user_id, permissions))
        except ValueError:
            messagebox.showwarning("Aviso", "IDs de grupo e usuário devem ser números inteiros.")
    else:
        messagebox.showwarning("Aviso", "Por favor, insira o token, o ID do grupo e o ID do usuário.")

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Promover Membro a Administrador")
root.geometry("400x500")

# Campo de entrada para o token do bot
tk.Label(root, text="Insira o Token do Bot:").pack(pady=5)
token_entry = tk.Entry(root, width=40)
token_entry.pack()

# Campo de entrada para o ID do grupo
tk.Label(root, text="Insira o ID do Grupo:").pack(pady=5)
group_id_entry = tk.Entry(root, width=40)
group_id_entry.pack()

# Campo de entrada para o ID do usuário
tk.Label(root, text="Insira o ID do Usuário:").pack(pady=5)
user_id_entry = tk.Entry(root, width=40)
user_id_entry.pack()

# Permissões como caixas de seleção
tk.Label(root, text="Selecione as permissões:").pack(pady=10)

can_change_info_var = tk.BooleanVar()
tk.Checkbutton(root, text="Pode mudar informações do grupo", variable=can_change_info_var).pack(anchor='w')

can_post_messages_var = tk.BooleanVar()
tk.Checkbutton(root, text="Pode postar mensagens", variable=can_post_messages_var).pack(anchor='w')

can_edit_messages_var = tk.BooleanVar()
tk.Checkbutton(root, text="Pode editar mensagens", variable=can_edit_messages_var).pack(anchor='w')

can_delete_messages_var = tk.BooleanVar()
tk.Checkbutton(root, text="Pode deletar mensagens", variable=can_delete_messages_var).pack(anchor='w')

can_invite_users_var = tk.BooleanVar()
tk.Checkbutton(root, text="Pode convidar usuários", variable=can_invite_users_var).pack(anchor='w')

can_restrict_members_var = tk.BooleanVar()
tk.Checkbutton(root, text="Pode restringir membros", variable=can_restrict_members_var).pack(anchor='w')

can_pin_messages_var = tk.BooleanVar()
tk.Checkbutton(root, text="Pode fixar mensagens", variable=can_pin_messages_var).pack(anchor='w')

can_promote_members_var = tk.BooleanVar()
tk.Checkbutton(root, text="Pode promover outros membros", variable=can_promote_members_var).pack(anchor='w')

# Botão para promover o membro a administrador
promover_button = tk.Button(root, text="Promover a Administrador", command=promover_admin)
promover_button.pack(pady=20)

# Executa a interface
root.mainloop()
