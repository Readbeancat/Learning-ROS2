#include <iostream>
#include <functional>

// free function
void free_function(const std::string& file_name)
{
    std::cout << "free_function: " << file_name << std::endl;
}

class FileSave
{
private:
    /* data */
public:
    FileSave(/* args */) = default;
    ~FileSave() = default;


    void member_function(const std::string& file_name)
    {
        std::cout << "free_function: " << file_name << std::endl;
    }
};


int main(){

    FileSave file_save;

    auto save_with_lambda = [](const std::string& file_name){
        std::cout << "save_with_lambda: " << file_name << std::endl;
    };


    free_function("file1.txt");
    file_save.member_function("file2.txt");
    save_with_lambda("file3.txt");


    std::function<void(const std::string&)> save1 = free_function;
    std::function<void(const std::string&)> save3 = save_with_lambda;

    //std::bind is used to bind a member function to an object
    std::function<void(const std::string&)> save2 = std::bind(&FileSave::member_function, &file_save, std::placeholders::_1);

    save1("file4.txt");
    save2("file5.txt");
    save3("file6.txt");

    return 0;
}