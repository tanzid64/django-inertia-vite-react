import { Link, usePage } from "@inertiajs/react";
import { PageProps as InertiaPageProps } from "@inertiajs/core";

interface IndexProps extends InertiaPageProps {
  app_name: string;
  user_count: number;
}

export default function Index() {
  const { app_name, user_count } = usePage<IndexProps>().props;

  return (
    <div>
      <h1>
        {app_name} : {user_count} users
      </h1>
      <h1>Welcome to the Home Page</h1>
      <Link href="/about">About</Link>
    </div>
  );
}
