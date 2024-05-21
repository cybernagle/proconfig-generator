# Makefile for Python package management

# Variables
PACKAGE_NAME = your_package_name  # 修改为你的包名

.PHONY: all clean build install uninstall

# 默认目标
all: clean build install

# 清理构建文件
clean:
	@echo "Cleaning up..."
	@rm -rf build dist *.egg-info
	@find . -name "__pycache__" -exec rm -rf {} +
	@find . -name "*.pyc" -exec rm -rf {} +
	@find . -name "*.pyo" -exec rm -rf {} +

# 构建包
build:
	@echo "Building the package..."
	@python setup.py sdist bdist_wheel

# 安装包
install:
	@echo "Installing the package..."
	@pip install .

# 卸载包
uninstall:
	@echo "Uninstalling the package..."
	@pip uninstall -y $(PACKAGE_NAME)

# 重新安装包
reinstall: uninstall install

# 发布到 PyPI
release: clean build
	@echo "Releasing the package to PyPI..."
	@twine upload dist/*

# 帮助信息
help:
	@echo "Makefile for Python package management"
	@echo ""
	@echo "Usage:"
	@echo "  make all        - Clean, build, and install the package"
	@echo "  make clean      - Clean up build artifacts"
	@echo "  make build      - Build the package"
	@echo "  make install    - Install the package"
	@echo "  make uninstall  - Uninstall the package"
	@echo "  make reinstall  - Reinstall the package"
	@echo "  make release    - Release the package to PyPI"
	@echo "  make help       - Show this help message"

