# main.py

from blog import Blog

def main():
    blog = Blog()

    while True:
        print("\nSimple Blogging Platform")
        print("1. Add Post")
        print("2. Edit Post")
        print("3. Delete Post")
        print("4. List Posts")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            blog.add_post(title, content)
            print("Post added successfully!")

        elif choice == "2":
            index = int(input("Enter post number to edit: ")) - 1
            new_title = input("Enter new post title (leave blank to keep current): ")
            new_content = input("Enter new post content (leave blank to keep current): ")
            if blog.edit_post(index, new_title, new_content):
                print("Post edited successfully!")
            else:
                print("Invalid post number.")

        elif choice == "3":
            index = int(input("Enter post number to delete: ")) - 1
            if blog.delete_post(index):
                print("Post deleted successfully!")
            else:
                print("Invalid post number.")

        elif choice == "4":
            blog.list_posts()

        elif choice == "5":
            print("Exiting Simple Blogging Platform.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
