<?hh

<<file:__EnableUnstableFeatures('require_constraint')>>

class C {
    use T;

    public function bar(): void {}
}

trait T {
    require this as C;

    public function foo(): void {
        $this->bar();
    }
}
