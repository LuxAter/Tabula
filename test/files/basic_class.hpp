#include <vector>

class A {
  A();
  ~A();
  class AB {
    AB(int A);
    ~AB();
  };
};

class B {
  // B(std::vector<int> b);
  ~B();
};
