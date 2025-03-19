#include <iostream>
#include <memory>

int main()
{
    auto p1 = std::make_shared<std::string>("It is a strings");
    std::cout << "p1: count" << p1.use_count() << "* pointer address"<< p1.get() << std::endl;

    auto p2 = p1;
    std::cout << "p1: count" << p1.use_count() << "* pointer address"<< p1.get() << std::endl;
    std::cout << "p2: count" << p2.use_count() << "* pointer address"<< p2.get() << std::endl;

    p1.reset();
    std::cout << "p1: count" << p1.use_count() << "* pointer address"<< p1.get() << std::endl;
    std::cout << "p2: count" << p2.use_count() << "* pointer address"<< p2.get() << std::endl;

    std::cout << "p2: " << p2->c_str() << std::endl;

    return 0;
}