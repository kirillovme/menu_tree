# Menu tree example

This project is a test task for UpTrader.

## Main Technologies Used

- Python
- Django
- PostgreSQL
- Docker

## Deploying the Project

### Requirements
- Docker and Docker Compose installed
- GNU Make

### Instructions:
1. Clone the repository
   ```bash
   git clone https://github.com/kirillovme/menu_tree.git
   ```
2. Start the containers
   ```bash
   make up-d
   ```
3. Create superuser via Makefile
    ```bash
   make createsuperuser    
    ```
4. Go to http://localhost:8000/admin and create following menu items
![Home](https://cdn.discordapp.com/attachments/800849536540868642/1174273942983286844/image.png?ex=6566fed4&is=655489d4&hm=8f4bae2e84604eb12652fb255eea9a2eff9ba43f40cea60851a2ae299169ccac&)
![About](https://cdn.discordapp.com/attachments/800849536540868642/1174274022444371998/image.png?ex=6566fee7&is=655489e7&hm=7cb1da89bd74ddad0ea835d031cd79a9cd1e5e6d693a48cabb5db4f0319ec1bd&)
![Careers](https://cdn.discordapp.com/attachments/800849536540868642/1174274072050413638/image.png?ex=6566fef3&is=655489f3&hm=92e1969b33197d7572bc0312ed739bda01323b59281826fea83bdecfb475fa76&)
![Our Team](https://cdn.discordapp.com/attachments/800849536540868642/1174274112768712714/image.png?ex=6566fefd&is=655489fd&hm=b75a21ac7b8c7dc3c9fdc10ecfe23975069d110d55b85150072ff9fd97c5d9fc&)
5. Go to http://localhost:8000/home to see the menu.




## Project Branch Structure

- `main` - Current production branch of the project
- `develop` - Main development branch
