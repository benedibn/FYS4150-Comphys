#include "EigenValueSolver.hpp"
#include <fstream>
#include <armadillo>
#include "EigenValueSolver.cpp"
#include "JacobiSolver.cpp"
#include "ArmaSolver.cpp"

using namespace std;
using namespace arma;

int main(int argc, char const *argv[]){
  double d = 2.;
  double a = -1.;
  int N = 5;
  ArmaSolver aTriMat(a,d,N);
  JacobiSolver aJacobi(a,d,N);
  vec eigen(N);
  vec eigen2(N);
  eigen = aTriMat.solve();
  for (int i = 0; i < N; i++){
    cout << eigen(i) << endl;
  }
  cout << "------------------------------\n";
  eigen2 = aJacobi.solve(100000);
  for (int i = 0; i < N; i++){
    cout << eigen2(i) << endl;
  }

  return 0;
}
