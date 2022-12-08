PWD:=$(shell pwd)
KERNEL_VER:=$(shell uname -r)
KERNEL_DIR:=/lib/modules/$(KERNEL_VER)/build
INSTALL_DIR:=/lib/modules/$(KERNEL_VER)/kernel/drivers/usb/ttyPos

obj-m := ttyPos.o

all:
	$(MAKE) modules -C $(KERNEL_DIR) M=$(PWD)
clean:
	$(MAKE) modules -C $(KERNEL_DIR) M=$(PWD) clean
install:
	install -D -m 644 ttyPos.ko $(INSTALL_DIR)/ttyPos.ko
	depmod -a
uninstall:
	modprobe -r ttyPos ; echo -n
	$(RM) $(INSTALL_DIR)/ttyPos.ko
	depmod -a
